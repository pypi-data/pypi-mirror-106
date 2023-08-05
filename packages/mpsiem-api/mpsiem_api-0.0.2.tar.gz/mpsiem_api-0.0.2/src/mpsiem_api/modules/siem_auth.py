import re
import html
import requests
from typing import Union
from logging import Logger

from mpsiem_api.modules.core import Core
from mpsiem_api.base_functions.base import LoggerHandler
from mpsiem_api.params.params import AUTHParams, SIEMSettings
from mpsiem_api.params.interfaces import AuthInterface, Credentials


class SIEMAuth(AuthInterface, SIEMSettings, LoggerHandler):
    """SIEMAuth Класс аутентификации в компонентах PTKB,CORE

    :param AuthInterface: Интерфейс аутентификации
    :param SIEMSettings: Опции MPSiem
    :param LoggerHandler: Опции логирования

    """

    __core_url = "/ui/login"
    __core_form_page = "/account/login?returnUrl=/#/authorization/landing"
    __core_check_url = "/api/deployment_configuration/v1/system_info"

    def __init__(
        self,
        siem_url: str,
        creds: Credentials,
        auth_type: AUTHParams,
        proxy: dict = None,
        logger: Logger = None,
    ) -> None:
        AuthInterface.__init__(self, creds)

        self.siem_url = siem_url
        self.__is_core_session_exists = False
        self.session = None
        self.auth_params = {
            "authType": auth_type.value,
            "username": creds.get("username"),
            "password": creds.get("password"),
            "newPassword": None,
        }
        self.proxy = proxy
        if logger is not None:
            self.logger = logger

    def connect(self, verify=True) -> Core:
        """connect Функция аутентификации в компонентe Core MPSiem"""
        core_object = self.__auth_core(verify=verify)
        return core_object

    @property
    def siem_url(self) -> str:
        """siem_url Getter для получения siem url

        :return: MPSiem url
        :rtype: str
        """
        return self.__siem_url

    @siem_url.setter
    def siem_url(self, siem_url: str) -> None:
        """siem_url Setter для параметра siem_url

        :param siem_url: Значение url siem
        :type siem_url: str
        """
        self.__siem_url = siem_url

    @property
    def proxy(self) -> dict:
        """proxy Getter для получения значений proxy

        :return: Словарь значений proxy
        :rtype: dict
        """
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy_settings: dict) -> None:
        """proxy Setter для присвоения значений proxy

        :param proxy_settings: Настройки для подключения через прокси
        :type proxy_options: dict
        """
        self.__proxy = proxy_settings

    @property
    def session(self) -> requests.Session:
        """session Getter для получения текущей сессии в MPSiem

        :return: Текущая сессия
        :rtype: requests.Session
        """
        if self.__session is not None:
            return self.__session
        else:
            self.logger.info("You don't have active session")

    @session.setter
    def session(self, session: requests.Session) -> None:
        """session Setter для присвоения значений сессии

        :param session: Значение для текущей сессии
        :type session: requests.Session
        """
        self.__session = session

    def disconnect(self) -> None:
        """disconnect Функция завершения сессии"""
        if self.session is not None:
            self.session.close()
        self.session = None

    def __auth_core(self, verify=True) -> None:
        """__auth_core Функция аутентификации в MPCore

        :raises Exception: Если введен неправильный пароль
        :raises Exception: Если отличается код ответа HTTP от 200
        :return: Объект класса Core
        :rtype: Core
        """

        auth_core_url = f"{self.siem_url}:{self.CORE_PORT}{self.__core_url}"
        auth_parse_form_url = f"{self.siem_url}{self.__core_form_page}"
        auth_status_url = f"{self.siem_url}{self.__core_check_url}"

        if self.__is_core_session_exists is False and self.session is None:
            self.session = requests.Session()
            self.session.verify = verify
            if self.proxy != None:
                self.session.proxies.update(self.proxy)
        else:
            self.logger.error("You already got active session in core")

        try:

            self.logger.info(f"Trying auth in core {auth_core_url}")
            auth_request = self.session.post(
                auth_core_url,
                json=self.auth_params,
            )
            if auth_request.json().get("message"):
                raise Exception(f'{auth_request.json().get("message")}')

            callback_url, core_query_params = self.__build_core_params(
                self.session.get(auth_parse_form_url).text
            )
            self.session.post(callback_url, data=core_query_params)

            auth_status = self.session.get(auth_status_url)
            if auth_status.status_code != 200:
                raise Exception(
                    self.logger.error("Received a response code error other than 200.")
                )

            self.__is_core_session_exists = True
            self.logger.info("Successful authentication in CORE")
            return Core(self.siem_url, self.session)

        except requests.RequestException as e:
            self.logger.error(e)

    def __build_core_params(self, response: requests.Response) -> Union[str, dict]:
        """__get_core_params Функция парсит ответ от GET запроса для получения параметров аутентификации в CORE

        :param response: Объект сессии
        :type response: requests.Response
        :return: Возврат URL 1 значением из поля action и возврат параметров 2ым значением
        :rtype: Union[str, dict]
        """

        return re.search("action=['\"]([^'\"]*)['\"]", response).groups()[0], {
            item.groups()[0]: html.unescape(item.groups()[1])
            for item in re.finditer(
                "name=['\"]([^'\"]*)['\"] value=['\"]([^'\"]*)['\"]", response
            )
        }
