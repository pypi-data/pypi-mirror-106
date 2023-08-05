import json
import requests
from typing import Union

from mpsiem_api.modules.events import EventFactory, Correlation, Event
from mpsiem_api.params.interfaces import Time
from mpsiem_api.params.params import LimitSettings, SIEMSettings
from mpsiem_api.base_functions.base import LoggerHandler, check_kwargs, build_query, _FILTER_QUERY


_KWARGS_FILTER_QUERY = [
    "filter",
    "full_query",
    "limit",
    "offset",
    "token",
    "parse_corr",
    "recursive",
    "key",
    "debug"
]

_HEADERS = {"Content-Type": "application/json;charset=UTF-8"}

class Core(SIEMSettings, LoggerHandler):

    __events = "/api/events/v2/events"

    def __init__(self, siem_url, session: requests.Session) -> None:

        self.session = session
        self.siem_url = siem_url
        self.headers = _HEADERS
        self.events_array = []

    @property
    def session(self) -> requests.Session:
        return self.__session

    @session.setter
    def session(self, session: requests.Session) -> None:
        self.__session = session

    @property
    def siem_url(self) -> str:
        return self.__siem_url

    @siem_url.setter
    def siem_url(self, url: str) -> None:
        self.__siem_url = url

    @property
    def headers(self) -> dict:
        return self.__headers

    @headers.setter
    def headers(self, headers: dict) -> None:
        self.__headers = headers

    def get_events(self, time_start: str, time_end: str, **kwargs) -> Union[Event, Correlation]:
        check_kwargs(_KWARGS_FILTER_QUERY, self.logger, **kwargs)
        kwargs["time_start"] = Time.get_unix_timestamp(time_start)
        kwargs["time_end"] = Time.get_unix_timestamp(time_end)
        for event in self.__create_query(**kwargs):
            yield event

    def __get_error_message_from_response(self, response, debug=False) -> str:
        message = "\"Unknown reason"
        if response.content == None:
            return message + " because of empty response content\""
        
        r = json.loads(response.content)
        if 'errors' not in r:
            return message + " because of missing errors section in response\""
        
        if type(r['errors']) is list and len(r['errors']) == 2:
            message = r['errors'][0]['error']['message']
            if debug:
                err = r['errors'][1]['error']
                message += "\nDetails:\n" + json.dumps(err, indent=4, sort_keys=True)
        else:
            message += " because unexpected error section structure"

        return message + "\""

    def __create_query(self, **kwargs) -> dict:

        if kwargs.get("limit") is None:
            kwargs["limit"] = LimitSettings.limit_events
        if kwargs.get("offset") is None:
            kwargs["offset"] = 0

        if kwargs.get("token") is not None:
            query_url = f"{self.siem_url}{self.__events}?limit={kwargs.get('limit')}&offset={kwargs.get('offset')}&token={kwargs.get('token')}"
        else:
            query_url = f"{self.siem_url}{self.__events}?limit={kwargs.get('limit')}&offset={kwargs.get('offset')}"

        if kwargs.get("full_query") is None:            
            query_params = build_query(_FILTER_QUERY, **kwargs)
        else:
            query_params = kwargs.get("full_query")

        query_result = self.session.post(query_url, query_params, headers=self.headers)

        if query_result.status_code != 200:
            message = self.__get_error_message_from_response(query_result, debug=kwargs.pop('debug', False))
            raise Exception(
                self.logger.error(
                    f"Bad request, got status code {query_result.status_code} with message {message}"
                )
            )

        if query_result.json().get("totalCount") == 0:
            self.logger.info(f"No data to return by filter {kwargs.get('filter')}")

        elif (
            query_result.json().get("totalCount") > kwargs.get("limit")
            and kwargs.get("offset") < query_result.json().get("totalCount")
            and kwargs.get("recursive") is True
        ):
            kwargs["token"] = query_result.json().get("token")
            self.logger.debug(
                f"Got events {query_result.json().get('totalCount')} more than limit {kwargs.get('limit')}, calculation offsets with step limit value"
            )

            for event in self.__get_subevents(
                query_result.json(),
                parse_corr=kwargs.get("parse_corr"),
            ):
                yield event

            while kwargs.get("offset") + kwargs.get("limit") < query_result.json().get(
                "totalCount"
            ):
                kwargs["offset"] += kwargs.get("limit")
                kwargs["time_end"] = """null"""
                for result in self.__create_query(**kwargs):
                    yield result

        else:
            for event in self.__get_subevents(
                query_result.json(), kwargs.get("parse_corr")
            ):
                yield event

    def _replace_filter(self, filter: str) -> str:
        if filter is None:
            filter = ""
        elif '\\"' in filter:
            pass
        else:
            filter = filter.replace('"', '\\"')
        return filter

    def __get_subevents(self, events: dict, parse_corr: bool = True):

        for event in events.get("events"):
            event = EventFactory.get_event_type(event)

            if isinstance(event, Correlation) and parse_corr is True:
                query_params = event.sub_events
                sub_events = self.session.post(
                    f"{self.siem_url}{query_params['sub_url']}",
                    query_params["params"],
                    headers=self.headers,
                )
                self.logger.debug(
                    f"Got correlation in query, getting sub events {sub_events.json().get('totalCount')}"
                )

                for sub_event in sub_events.json().get("events"):
                    yield EventFactory.get_event_type(sub_event)
            else:
                yield event
