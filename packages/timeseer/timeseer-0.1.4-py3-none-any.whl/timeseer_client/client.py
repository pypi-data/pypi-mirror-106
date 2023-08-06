"""Timeseer Client allows querying of data and metadata."""

import json

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

from kukur import InterpolationType, SeriesSelector
from kukur.client import Client as KukurClient

import pyarrow.flight as fl
try:
    import pandas as pd
    import timeseer_client.filters_pandas as filters_pandas
    HAS_PANDAS = True
except Exception:  # pylint: disable=broad-except
    HAS_PANDAS = False

import timeseer_client.filters_arrow as filters_arrow
from .base import AugmentationStrategy, UnknownAugmentationStrategyException


class Client(KukurClient):
    """Client connects to Timeseer using Arrow Flight."""

    def get_event_frames(
        self,
        start_date: datetime = None,
        end_date: datetime = None,
        frame_type: str = None,
        selector: SeriesSelector = None,
    ):
        """Get all event frames matching the given criteria.

        Args:
            start_date: the start date of the range to find overlapping event frames in. Defaults to one year ago.
            end_date: the end date of the range to find overlapping event frames in. Defaults to now.
            frame_type: the type of event frames to search for. Finds all types when empty.
            selector: the time series source or time series to which the event frames are linked.
                Matches all by default.

        Returns::
            A pyarrow Table with 5 columns.
            The first column ('start_date') contains the start date.
            The second column ('end_date') contains the end date.
            The third column ('type') contains the type of the returned event frame as a string.
            Columns 4 ('series_source') and 5 ('series_name') contain the source and name of the series.
        """
        if start_date is None or end_date is None:
            now = datetime.utcnow().replace(tzinfo=timezone(timedelta(0)))
            if start_date is None:
                start_date = now.replace(year=now.year-1)
            if end_date is None:
                end_date = now

        query: Dict[str, Any] = {
            'query': 'get_event_frames',
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat(),
        }

        if frame_type is not None:
            query['type'] = frame_type
        if selector is not None:
            query['selector'] = {
                'source': selector.source,
            }
            if selector.name is not None:
                query['selector']['name'] = selector.name

        ticket = fl.Ticket(json.dumps(query))
        return self._get_client().do_get(ticket).read_all()

    def get_data_quality_score_data_sources(self, source_names: List[str]):
        """Get the data quality score of a data source.

        Args:
            source_names: A list of time series sources

        Returns::
            A data quality score of every given source in percentage.
        """
        body = {
            'source_names': source_names,
        }
        results = list(self._get_client().do_action(("get_data_quality_score_data_sources", json.dumps(body).encode())))
        return json.loads(results[0].body.to_pybytes())

    def get_kpi_scores(
        self,
        source_name: str,
    ):
        """Get the kpi scores of a data source.

        Args:
            source_name: The time series source

        Returns::
            The score per KPI for the source in percentage.
        """
        body = {
            'source_name': source_name,
        }

        results = list(self._get_client().do_action(("get_kpi_scores", json.dumps(body).encode())))
        return json.loads(results[0].body.to_pybytes())

    def get_data_quality_score_project(self, project_name: str,):
        """Get the data quality score of a data source.

        Args:
            project_name: The name of the project in Timeseer.

        Returns::
            The data quality score of the project in percentage.
        """
        body = {
            'project_name': project_name,
        }
        results = list(self._get_client().do_action(("get_data_quality_score_project", json.dumps(body).encode())))
        return json.loads(results[0].body.to_pybytes())


def filter_series(
        series,
        event_frames,
        augmentation_strategy: AugmentationStrategy = AugmentationStrategy.REMOVE,
        interpolation_type: Optional[InterpolationType] = None,
        context: Optional[List[pd.DataFrame]] = None
):
    """Filter the time series in the time periods given by event_frames

        Args:
            series: a pyarrow Table or a pandas DataFrame with time series date
                Two columns are present: 'ts' and 'value'.
                A pandas DataFrame can contain a DatetimeIndex instead of the 'ts' column.
            event_frames: pyarrow Table or a pandas DataFrame with event frames.
                Three columns need to be present: 'type', 'start_date' and 'end_date'.
            augmentation_strategy: An enum to define which strategy to use when filtering.
                'REMOVE' (the default) removes the values, 'HOLD_LAST' keeps the last acceptable value and
                'LINEAR_INTERPOLATION' interpolates the last acceptable value and the next acceptable value.
                If no acceptable value exists, they are removed. 'KNN_IMPUTATION' uses context to find the
                k-nearest neighbors and takes the average.
            interpolation_type: Enum to define the interpolation type. 'LINEAR' or 'STEPPED'.
                Only linear interpolation types can be linearly interpolated in the augmentation strategy.
            context: A list of pd.DataFrame used for 'KNN_IMPUTATION' to find nearest neighbors
        Returns:
            A filtered pyarrow Table or a pandas DataFrame with 2 columns: 'ts' and 'value'.
            In case the pandas DataFrame provided in 'series' has a DatetimeIndex,
                the 'ts' column will not be present, but the DataFrame will have a DateTimeIndex.
    """
    if context is None:
        context = []

    if not isinstance(augmentation_strategy, AugmentationStrategy):
        raise UnknownAugmentationStrategyException()

    if augmentation_strategy == AugmentationStrategy.LINEAR_INTERPOLATION and \
       interpolation_type != InterpolationType.LINEAR:
        augmentation_strategy = AugmentationStrategy.HOLD_LAST

    if len(series) == 0:
        return series

    if(HAS_PANDAS and isinstance(series, pd.DataFrame) and isinstance(event_frames, pd.DataFrame)):
        return filters_pandas.filter_series(series, event_frames, augmentation_strategy, context)
    return filters_arrow.filter_series(series, event_frames, augmentation_strategy)


def filter_event_frames(
        event_frames,
        start_date: datetime,
        end_date: datetime
):
    """Restrict the event frames to the given time range.

        Args:
            event_frames: a pyarrow Table or a pandas DataFrame with event frames.
            start_date: the start date of the range to filter event_frames.
            end_date: the end date of the range to filter event_frames.

        Returns::
            A filtered pyarrow Table or a pandas DataFrame with 5 columns.
            The first column ('start_date') contains the 'start_date' and 'end_date'.
            The second column ('end_date') contains the 'end_date'.
            The third column ('type') contains the type of the returned event frame as a string.
            Columns 4 ('series_source') and 5 ('series_name') contain the source and name of the series.
    """
    if(HAS_PANDAS and isinstance(event_frames, pd.DataFrame)):
        return filters_pandas.filter_event_frames(event_frames, start_date, end_date)
    return filters_arrow.filter_event_frames(event_frames, start_date, end_date)
