from typing import Union

from mpsiem_api.params.interfaces import EventInterface
from mpsiem_api.base_functions.base import _FILTER_QUERY, LoggerHandler, build_query


class Event(EventInterface):
    @property
    def msgid(self) -> str:
        return self.event_data.get("msgid")

    @property
    def event_title(self) -> str:
        return self.event_data.get("event_src.title")


class Correlation(EventInterface):
    @property
    def corr_name(self) -> str:
        return self.event_data.get("correlation_name")

    @property
    def detect(self) -> str:
        return self.event_data.get("detect")

    @property
    def corr_type(self) -> str:
        return self.event_data.get("correlation_type")

    @property
    def sub_events(self) -> dict:
        sub_url = f"/api/events/v2/subevents/{self.uuid}?field=subevents&eventId={self.uuid}&limit=100&offset=0"
        params = build_query(_FILTER_QUERY)
        return dict(sub_url=sub_url, params=params)


class EventFactory(LoggerHandler):
    @staticmethod
    def get_event_type(event: dict) -> Union[Event, Correlation]:
        if event.get("correlation_name") != None:
            return Correlation(event)
        else:
            return Event(event)
