from datetime import datetime

from mpsiem_api.base_functions.base import LoggerHandler


class Time:
    @staticmethod
    def get_sync_time() -> datetime:
        """get_current_time Функция для показа текущего времени

        Returns:
            str: Текущее время в формате деплой лога PTKB
        """
        return datetime.today().strftime("%Y-%m-%dT%H:%M:%S.%f")

    @staticmethod
    def get_short_date() -> datetime:
        return datetime.today().strftime("%d.%m.%Y")

    @staticmethod
    def get_unix_timestamp(time: datetime) -> int:
        return int(datetime.strptime(str(time), "%Y-%m-%d %H:%M:%S.%f").timestamp())


class Credentials:
    """Интерфейс для параметров аутентификации"""

    def __init__(self, params: dict = None) -> None:

        self.username = None
        self.password = None

        if params is not None:
            self.username = params["username"]
            self.password = params["password"]


class AuthInterface:
    """Интерфейс класса аутентификации"""

    def __init__(self, creds: Credentials) -> None:
        self.creds = creds

    def connect(self):
        pass

    def disconnect(self):
        pass

class EventInterface(LoggerHandler):
    """Интерфейс событий из MP EventViewer"""

    def __init__(self, event_data) -> None:
        self.event_data = event_data

    @property
    def event_data(self) -> dict:
        return self.__event_data

    @event_data.setter
    def event_data(self, event_data: dict) -> None:
        self.__event_data = event_data

    @property
    def event_host(self) -> str:
        return self.event_data.get("event_src.host")

    @property
    def uuid(self) -> str:
        return self.event_data.get("uuid")

    @property
    def time(self) -> datetime:
        return self.event_data.get("time")