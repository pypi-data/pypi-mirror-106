import os
import logging
from random import choice
from starlette.config import Config as StarletteConfig
from starlette.datastructures import CommaSeparatedStrings, Secret
from starlette.middleware import Middleware


class _Config(dict):
    def __init__(self):
        super().__init__()

        self._cfg = StarletteConfig()

        # --- APP Config ---
        # APP_NAME must be unique for all the application modules
        self.env_string("RW_APP_NAME", default="RedWarden")

        # --- MODULE Config ---
        self["RW_MODULE_PATH"] = os.getcwd()
        self.env_string("RW_MODULE_NAME", default="RedWardenModule")
        self.env_string("RW_MODULE_ENV", default="production")
        self.env_bool("RW_MODULE_DEBUG")
        self.env_string("RW_MODULE_LOG_LEVEL", default="INFO")
        self.env_string(
            "RW_MODULE_LOG_FORMAT",
            default=(
                "%(levelname) -8s %(asctime)s [ %(lineno) -5d] %(pathname) -50s: %(message)s"
            ),
        )  # %(thread)d for thread ID

        # --- VIEWS Config
        self["RW_VIEWS_TEMPLATE_DIR"] = os.getcwd() + "/views"

    def env_string(self, name, default=None):
        self[name] = self._cfg(name, default=default)

    def env_string_list(self, name, default=None):
        self[name] = self._cfg(name, cast=CommaSeparatedStrings, default=default or [])

    def env_bool(self, name, default=False):
        self[name] = self._cfg(name, cast=bool, default=default)

    def env_int(self, name, default=0):
        self[name] = self._cfg(name, cast=int, default=default)

    def env_secret(self, name):
        self[name] = self._cfg(name, cast=Secret, default=None)


Config = _Config()

Logger = logging.getLogger(Config["RW_APP_NAME"])
Logger.setLevel(Config["RW_MODULE_LOG_LEVEL"])
_logger_handler = logging.StreamHandler()
Logger.addHandler(_logger_handler)
_logger_handler.setFormatter(logging.Formatter(Config["RW_MODULE_LOG_FORMAT"]))


class Backends:
    _backends = {}

    @classmethod
    def get(cls, backend_name, additional_params=None, raise_if_missing=True):
        backend = cls._backends.get(backend_name, None)
        if not backend:
            if raise_if_missing:
                raise Exception("Backend %s does not exist" % backend_name)
            return None

        endpoint = choice(backend["endpoints"])
        params = backend["params"]
        if additional_params:
            params.update(additional_params)

        return backend["class"](endpoint, params)

    @classmethod
    def add(cls, backend_name, backend_class, endpoints, params=None):
        if not endpoints:
            raise Exception("No endpoints specified for backend %s" % backend_name)
        if isinstance(endpoints, str):
            endpoints = endpoints.split(",")
        elif not isinstance(endpoints, list):
            endpoints = [endpoints]

        backend = cls._backends.get(backend_name, None)
        if backend:
            raise Exception("Backend %s already exists" % backend_name)

        cls._backends[backend_name] = {
            "class": backend_class,
            "endpoints": endpoints,
            "params": params or {},
        }


class RedWardens:
    _red_wardens = {}

    @classmethod
    def get_endpoint(cls, red_warden_module_name, raise_if_missing=True):
        rw = cls._red_wardens.get(red_warden_module_name, None)
        if not rw:
            if raise_if_missing:
                raise Exception(
                    "RedWarden module %s does not exist" % red_warden_module_name
                )
            return None

        return choice(rw)

    @classmethod
    def add(cls, red_warden_module_name, endpoints):
        if not endpoints:
            raise Exception(
                "No endpoints specified for RedWarden module %s"
                % red_warden_module_name
            )
        if isinstance(endpoints, str):
            endpoints = endpoints.split(",")
        elif not isinstance(endpoints, list):
            endpoints = [endpoints]

        rw = cls._red_wardens.get(red_warden_module_name, None)
        if rw:
            raise Exception(
                "RedWarden module %s already exists" % red_warden_module_name
            )

        cls._red_wardens[red_warden_module_name] = endpoints


class Engines:
    _engines = {}

    @classmethod
    def get_all(cls):
        return cls._engines

    @classmethod
    def get(cls, engine_name, raise_if_missing=True):
        engine = cls._engines.get(engine_name, None)
        if raise_if_missing and not engine:
            raise Exception("Engine %s does not exist" % engine_name)
        return engine

    @classmethod
    def add(cls, engine_name, engine):
        cls._engines[engine_name] = engine


class Middlewares:
    _middlewares = []

    @classmethod
    def get_all(cls):
        return cls._middlewares

    @classmethod
    def add(cls, middleware, **options):
        cls._middlewares.append(Middleware(middleware, **options))


class Datazones:
    _datazones = {}

    @classmethod
    def add(cls, datazone_name):
        if datazone_name not in cls._datazones.keys():
            cls._datazones[datazone_name] = {}

    @classmethod
    def configure(cls, datazone_name, options=None, used_by="GLOBAL"):
        if datazone_name not in cls.get_names():
            raise Exception("Datazone %s does not exists." % datazone_name)

        cls._datazones[datazone_name][used_by] = options

    @classmethod
    def get_names(cls):
        return cls._datazones.keys()

    @classmethod
    def get_configuration(cls, datazone_name, used_by="GLOBAL"):
        if datazone_name not in cls.get_names():
            raise Exception("Datazone %s does not exists." % datazone_name)

        if used_by not in cls._datazones[datazone_name]:
            raise Exception(
                "Configuration %s for datazone %s does not exists."
                % (used_by, datazone_name)
            )

        return cls._datazones[datazone_name][used_by]
