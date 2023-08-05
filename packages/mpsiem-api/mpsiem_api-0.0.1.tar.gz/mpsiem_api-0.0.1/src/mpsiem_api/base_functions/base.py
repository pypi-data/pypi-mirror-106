import sys
import json
import logging
from jinja2 import Template


def check_kwargs(allow_list: list, logger: logging.Logger, **kwargs) -> None:
    """check_kwargs Функция для проверки валидности списка аргументов kwargs

    Args:
        allow_list (list): Список допустимых значений ключей
        logger (logging.Logger): Объект логгера

    Raises:
        Exception: Если ключ не входит в список допустимых значений
    """
    for key in kwargs.keys():
        if key not in allow_list:
            raise AssertionError(
                logger.error(
                    f"Not allowed kwargs argument {key}. Allowed values: {allow_list}"
                )
            )


######################################################################
### CORE QUERY
######################################################################

_FILTER_QUERY = """
{
    "filter": {
        "select": [
            {%- if data.get('fields') != None %}
                {%- for field in data.get('fields') %}
            "{{ field }}", 
                {%- endfor %}
            {%- else %}            
            "action",
            "agent_id",
            "aggregation_name",
            "asset_ids",
            "assigned_dst_host",
            "assigned_dst_ip",
            "assigned_dst_port",
            "assigned_src_host",
            "assigned_src_ip",
            "assigned_src_port",
            "category.generic",
            "category.high",
            "category.low",
            "chain_id",
            "correlation_name",
            "correlation_type",
            "count",
            "count.bytes",
            "count.bytes_in",
            "count.bytes_out",
            "count.packets",
            "count.packets_in",
            "count.packets_out",
            "count.subevents",
            "datafield1",
            "datafield10",
            "datafield2",
            "datafield3",
            "datafield4",
            "datafield5",
            "datafield6",
            "datafield7",
            "datafield8",
            "datafield9",
            "detect",
            "direction",
            "dst.asset",
            "dst.fqdn",
            "dst.geo.asn",
            "dst.geo.city",
            "dst.geo.country",
            "dst.geo.org",
            "dst.host",
            "dst.hostname",
            "dst.ip",
            "dst.mac",
            "dst.port",
            "duration",
            "event_src.asset",
            "event_src.category",
            "event_src.fqdn",
            "event_src.host",
            "event_src.hostname",
            "event_src.id",
            "event_src.ip",
            "event_src.subsys",
            "event_src.title",
            "event_src.vendor",
            "event_type",
            "external_link",
            "generator",
            "generator.type",
            "generator.version",
            "historical",
            "id",
            "importance",
            "incorrect_time",
            "input_id",
            "interface",
            "job_id",
            "logon_auth_method",
            "logon_service",
            "logon_type",
            "mime",
            "msgid",
            "nas_fqdn",
            "nas_ip",
            "normalized",
            "object",
            "object.account.contact",
            "object.account.dn",
            "object.account.domain",
            "object.account.fullname",
            "object.account.group",
            "object.account.id",
            "object.account.name",
            "object.account.privileges",
            "object.account.session_id",
            "object.domain",
            "object.fullpath",
            "object.group",
            "object.hash",
            "object.id",
            "object.name",
            "object.path",
            "object.process.cmdline",
            "object.process.cwd",
            "object.process.fullpath",
            "object.process.guid",
            "object.process.hash",
            "object.process.id",
            "object.process.meta",
            "object.process.name",
            "object.process.original_name",
            "object.process.parent.cmdline",
            "object.process.parent.fullpath",
            "object.process.parent.guid",
            "object.process.parent.hash",
            "object.process.parent.id",
            "object.process.parent.name",
            "object.process.parent.path",
            "object.process.path",
            "object.process.version",
            "object.property",
            "object.query",
            "object.state",
            "object.type",
            "object.value",
            "object.vendor",
            "object.version",
            "original_time",
            "protocol",
            "protocol.layer7",
            "reason",
            "recv_asset",
            "recv_host",
            "recv_ipv4",
            "recv_ipv6",
            "recv_time",
            "remote",
            "scope_id",
            "siem_id",
            "site_address",
            "site_alias",
            "site_id",
            "site_name",
            "src.asset",
            "src.fqdn",
            "src.geo.asn",
            "src.geo.city",
            "src.geo.country",
            "src.geo.org",
            "src.host",
            "src.hostname",
            "src.ip",
            "src.mac",
            "src.port",
            "start_time",
            "status",
            "subevents",
            "subject",
            "subject.account.contact",
            "subject.account.dn",
            "subject.account.domain",
            "subject.account.fullname",
            "subject.account.group",
            "subject.account.id",
            "subject.account.name",
            "subject.account.privileges",
            "subject.account.session_id",
            "subject.domain",
            "subject.group",
            "subject.id",
            "subject.name",
            "subject.privileges",
            "subject.process.cmdline",
            "subject.process.cwd",
            "subject.process.fullpath",
            "subject.process.guid",
            "subject.process.hash",
            "subject.process.id",
            "subject.process.meta",
            "subject.process.name",
            "subject.process.original_name",
            "subject.process.parent.cmdline",
            "subject.process.parent.fullpath",
            "subject.process.parent.guid",
            "subject.process.parent.hash",
            "subject.process.parent.id",
            "subject.process.parent.name",
            "subject.process.parent.path",
            "subject.process.path",
            "subject.process.version",
            "subject.state",
            "subject.type",
            "subject.version",
            "tag",
            "task_id",
            "taxonomy_version",
            "tcp_flag",
            "tenant_id",
            "text",
            "time",
            "type",
            "uuid",
            {%- endif %}
        ],
        {%- if data.get('filter') != None %}
        "where": {{ data.get('filter') }},
        {%- else %}
        "where": "",
        {%- endif %}
        {%- if data.get('order_by') != None %}
        "orderBy": [{"field": "{{ data.get('order_by').filed }}", "sortOrder": "{{ data.get('order_by').direction }}"}],
        {%- else %}
        "orderBy": [{"field": "time", "sortOrder": "descending"}],
        {%- endif %}
        {%- if data.get('group_by') != None %}
        "groupBy": [
                {%- for field in data.get('group_by') %}
            "{{ field.name }}", 
                {%- endfor %}
            ],
        {%- else %}
        "groupBy": [],
        {%- endif %}
        {%- if data.get('aggregate_by') != None %}
        "aggregateBy": [{
                "function": "{{ data.get('aggregate_by').function }}",
                "field": "{{ data.get('aggregate_by').field }}",
                "unique": {{ data.get('aggregate_by').unique }}
            }
        ],
        {%- else %}
        "aggregateBy": [],
        {%- endif %}
        {%- if data.get('distribute_by') != None %}
        "distributeBy": [{
                "field": "{{ data.get('distribute_by').field }}",
                "granularity": "{{ data.get('distribute_by').granularity }}"
            }
        ],
        {%- else %}
        "distributeBy": [],
        {%- endif %}
        "top": null,
        "aliases": {
        {%- if data.get('group_by') != None %}
            "groupBy": {
            {%- for field in data.get('group_by') %}
                {%- if field.alias != None %}
                "{{ field.name }}": "{{ field.alias }}",
                {%- endif %} 
            {%- endfor %}
            }
        {%- endif %}
        {%- if data.get('aggregate_by') != None %}
        ,
            "aggregateBy": {
                {%- if data.get('aggregate_by').alias != None %}
                "{{ data.get('aggregate_by').field }}": "{{ data.get('aggregate_by').alias }}"
                {%- endif %}
            }
        {%- endif %}
        }
    },
    "groupValues": [],
    {%- if data.get('time_start') != None %}
    "timeFrom": {{ data.get('time_start') }},
    {%- endif %}
    {%- if data.get('time_end') != None %}
    "timeTo": {{ data.get('time_end') }},
    {%- endif %}
}
"""

######################################################################
### BUILD QUERY FUNCTION
######################################################################


def build_query(template: str, **kwargs) -> str:
    """_build_query Функция построения запроса

    Kwargs:
    limit - лимит выгрузки
    search - строковый поиск по названию
    search_regex - строковый поиск по регулярному выражению внутри правила
    object_type - тип объекта PTKB, перебирается через Enum
    deployment_status - статус установки в PTKB
    packet_name - название пакета экспертизы
    multi_thread - включить мультипоточность
    thread_pool - количество потоков
    :param template: Jinja шаблон
    :type template: str
    :return: Заполненный опциями kwargs текст шаблона
    :rtype: str
    """
    kwargs["filter"] = json.dumps(kwargs["filter"])
    return Template(template).render(data=kwargs)


######################################################################
### Logging
######################################################################


FORMATTER = logging.Formatter(
    "%(asctime)s - %(process)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

LEVEL = "DEBUG"

def get_console_handler() -> logging.StreamHandler:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

class LoggerHandler():
    """Класс, создающий logger объект при наследовании"""
    logger = logging.getLogger(__name__)
    logger.setLevel(LEVEL)
    logger.addHandler(get_console_handler())
    logger.propagate = False
