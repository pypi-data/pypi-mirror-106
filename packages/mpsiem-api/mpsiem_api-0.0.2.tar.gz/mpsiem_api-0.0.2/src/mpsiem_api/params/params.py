from enum import Enum


_TEMPLATE_DIRECTORY = "..\\..\\jinja_templates"


class LimitSettings:

    limit_ptkb_objects = 1000
    limit_tabular_rows = 2000
    limit_deploy_logs = 50
    limit_macros = 100
    limit_events = 100
    limit_incidents = 50
    limit_threads = 4


class SIEMSettings:
    """SIEMOptions Стандартные порты SIEM"""

    PTKB_PORT = 8091
    CORE_PORT = 3334


class AUTHParams(Enum):
    """AUTHParams Параметры аутентификации в MPSIEM"""

    LOCAL = 0
    LDAP = 1



class JinjaSettings:

    template_directory_path = _TEMPLATE_DIRECTORY
