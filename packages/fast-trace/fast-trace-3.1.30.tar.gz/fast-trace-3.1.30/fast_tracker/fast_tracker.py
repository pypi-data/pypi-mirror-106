#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by FAST-DEV 2021/4/12
"""

from fast_tracker import config, Layer, ComponentType, Log, LogItem
from fast_tracker.trace.context import get_context
from fast_tracker.trace.tags import Tag
from fast_tracker.utils import functions


class FastTracker:
    def __init__(self):
        self.span = None

    @property
    def product_code(self):
        """
        获取 product_code 值
        :return:
        """
        return config.product_code

    @product_code.setter
    def product_code(self, product_code: str = ""):
        """
        设置 product_code 值
        :param product_code:
        :return:
        """
        config.set_product_code(product_code)

    @property
    def app_code(self):
        """
        获取 app_code 值
        :return:
        """
        return config.app_code

    @app_code.setter
    def app_code(self, app_code: str = ""):
        """
        设置 app_code 值
        :param app_code:
        :return:
        """
        config.set_app_code(app_code)

    @property
    def env_code(self):
        """
        获取 env_code 值
        :return:
        """
        return config.custom_env_code if config.custom_env_code else config.env_code

    @env_code.setter
    def env_code(self, env_code: str = ""):
        """
        设置 env_code 值
        :param env_code:
        :return:
        """
        if env_code:
            config.custom_env_code = env_code

    @property
    def tenant_code(self):
        """
        获取 tenant_code 值
        :return:
        """
        return config.custom_tenant_code if config.custom_tenant_code else config.tenant_code

    @tenant_code.setter
    def tenant_code(self, tenant_code: str = ""):
        """
        设置 tenant_code 值
        :param tenant_code:
        :return:
        """
        if tenant_code:
            config.custom_tenant_code = tenant_code

    @property
    def user_code(self):
        """
        获取 user_code 值
        :return:
        """
        return config.custom_user_code if config.custom_user_code else config.user_code

    @user_code.setter
    def user_code(self, user_code: str = ""):
        """
        设置 user_code 值
        :param user_code:
        :return:
        """
        if user_code:
            config.custom_user_code = user_code

    @property
    def service_name(self):
        """
        获取 service_name 值
        :return:
        """
        return config.service_name

    @service_name.setter
    def service_name(self, service_name: str = ""):
        """
        设置 service_name 值
        :param service_name:
        :return:
        """
        config.set_service_name(service_name)

    @property
    def socket_path(self):
        """
        获取 socket_path 值
        :return:
        """
        return config.collector_address

    @socket_path.setter
    def socket_path(self, socket_path: str = ""):
        """
        设置 socket_path 值
        :param socket_path:
        :return:
        """
        config.set_socket_path(socket_path)

    @property
    def buffer_size(self):
        """
        获取 buffer_size 值
        :return:
        """
        return config.buffer_size

    @buffer_size.setter
    def buffer_size(self, buffer_size: int = 1):
        """
        设置 buffer_size 值
        :param buffer_size:
        :return:
        """
        config.set_buffer_size(buffer_size)

    @property
    def socket_timeout(self):
        """
        获取 socket_timeout 值
        :return:
        """
        return config.socket_timeout

    @socket_timeout.setter
    def socket_timeout(self, socket_timeout: int = 1):
        """
        设置 socket_timeout 值
        :param socket_timeout:
        :return:
        """
        config.set_socket_timeout(socket_timeout)

    @property
    def event(self):
        """
        获取 event 值
        :return:
        """
        return config.event

    @event.setter
    def event(self, event: dict):
        """
        设置 event 值
        :param event:
        :return:
        """
        config.set_event(event)

    def get_config(self):
        return {
            "ServiceName": config.service_name,
            "TrackerVersion": config.tracker_version,
            "ServiceInstance": config.service_instance,
            "Protocol": config.protocol,
            "LoggingLevel": config.logging_level,
            "IgnoreSuffix": config.ignore_suffix,
            "CorrelationElementMaxNumber": config.correlation_element_max_number,
            "CorrelationValueMaxLength": config.correlation_value_max_length,
            "TraceIgnorePath": config.trace_ignore_path,
            "Enable": config.enable,
            "Debug": config.debug,
            "DebugLevel": config.debug_level,
            "EnvCode": config.env_code,
            "TenantCode": config.tenant_code,
            "UserCode": config.user_code,
            "SocketPath": config.collector_address,
            "BufferSize": config.buffer_size,
            "SocketTimeout": config.socket_timeout,
            "Event": config.event,
            "TenantCodeReader": config.tenant_code_reader,
            "UserCodeReader": config.user_code_reader,
            "EnvCodeReader": config.env_code_reader,
            "CarrierHeader": config.carrier_header,
        }

    def begin_span(self, operation: str = ""):
        """
        log模块开始 类似数据库事务的begin_trasaction
        :param op:
        :return:
        """
        try:
            if "custom_event" in config.disable_plugins:
                functions.log("已在配置Event-Components-CustomEvent中关闭此项")
                return False
            if not operation:
                functions.log("operation参数必填")
                return False
            context = get_context()
            self.span = context.new_local_span(op="execute")
            self.span.layer = Layer.Local
            self.span.component = ComponentType.CustomEvent
            self.span.op = operation
            self.span.start()
            return self
        except Exception as e:
            functions.log("调用begin_span时发生错误，错误信息:%r", str(e))

    def set_component(self, name: str = "CustomEvent"):
        if type(name) is not str:
            functions.log("传入参数类型不匹配，只允许传入str类型参数")
            return False
        if not name:
            functions.log("name为空")
            return False
        if "custom_event" in config.disable_plugins:
            functions.log("已在配置Event-Components-CustomEvent中关闭此项")
            return False
        if not self.span:
            functions.log("请先调用begin_span进行实例化")
            return False
        self.span.component = name

    def add_tag(self, key: str = "", val: str = ""):
        if type(key) is not str or type(val) is not str:
            functions.log("传入参数类型不匹配，只允许传入str类型参数")
            return False
        if not key or not val:
            functions.log("key或val为空")
            return False
        if "custom_event" in config.disable_plugins:
            functions.log("已在配置Event-Components-CustomEvent中关闭此项")
            return False
        if not self.span:
            functions.log("请先调用begin_span进行实例化")
            return False
        try:
            self.span.tag(Tag(key=key, val=val, overridable=True))
        except Exception as e:
            functions.log("调用add_tag时发生错误，错误信息:%r", str(e))

    def add_log(self, message: str = ""):
        if type(message) is not str:
            functions.log("传入参数类型不匹配，只允许传入str类型参数")
            return False
        if not message:
            functions.log("message为空")
            return False
        if "custom_event" in config.disable_plugins:
            functions.log("已在配置Event-Components-CustomEvent中关闭此项")
            return False
        if not self.span:
            functions.log("请先调用begin_span进行实例化")
            return False
        self.span.logs.append(Log(items=[LogItem(key="Logging", val=self.log_covert(message, err_type=""))]))

    def error_occurred(self, error: Exception):
        if not error:
            functions.log("参数为空")
            return False
        if type(error) is not Exception:
            functions.log("传入参数类型不匹配，只允许传入Exception类型参数")
            return False
        if "custom_event" in config.disable_plugins:
            functions.log("已在配置Event-Components-CustomEvent中关闭此项")
            return False
        if not self.span:
            functions.log("请先调用begin_span进行实例化")
            return False
        self.span.log(error)

    def log_covert(self, msg: str = "", err_type: str = "DEBUG"):
        return {"err_msg": msg, "err_type": err_type if err_type else "", "err_trace": ""}

    def end_span(self):
        """
        log模块结束
        :return:
        """
        if "custom_event" in config.disable_plugins:
            functions.log("已在配置Event-Components-CustomEvent中关闭此项")
            return False
        if not self.span:
            functions.log("请先调用begin_span进行实例化")
            return False
        self.span.stop()

    log_level = {"NOTSET": 0, "DEBUG": 10, "INFO": 20, "WARNING": 30, "WARN": 30, "ERROR": 40, "CRITICAL": 50}

    def debug(self, msg: str = ""):
        self.__logging(msg, err_type="DEBUG")

    def info(self, msg: str = ""):
        self.__logging(msg, err_type="INFO")

    def warning(self, msg: str = ""):
        self.__logging(msg, err_type="WARNING")

    def warn(self, msg: str = ""):
        self.warning(msg)

    def error(self, msg: str = ""):
        self.__logging(msg, err_type="ERROR")

    def critical(self, msg: str = ""):
        self.__logging(msg, err_type="CRITICAL")

    def __logging(self, msg: str = "", err_type: str = ""):
        try:
            if not msg:
                functions.log("参数为空")
                return False
            if type(msg) is not str:
                functions.log("传入参数类型不匹配，只允许传入str类型参数")
                return False
            config_log_type = FastTracker.log_level.get(config.logging_level)
            cus_log_type = FastTracker.log_level.get(err_type)
            if config_log_type > cus_log_type:
                return False
            if "fast_log" in config.disable_plugins:
                functions.log("已在配置Event-Components-Logging中关闭此项")
                return False
            context = get_context()
            if not context:
                functions.log("探针未启动")
                return False
            with context.new_local_span(op="Logging") as span:
                span.layer = Layer.Local
                span.component = ComponentType.Log
                span.logs.append(Log(items=[LogItem(key="Logging", val=self.log_covert(msg, err_type=err_type))]))
        except Exception as e:
            functions.log("__logging发生错误，错误信息:%r", str(e))
