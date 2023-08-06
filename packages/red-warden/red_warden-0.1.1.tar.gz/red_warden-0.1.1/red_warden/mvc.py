from abc import ABC
import sqlalchemy
import graphene
from mako.lookup import TemplateLookup
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount
from red_warden.config import Config, Datazones
from red_warden.i18n import RWMemoryI18n

# Database table definitions.
metadata = sqlalchemy.MetaData()


# --- CONTROLLERS ------------------------------------------------------------------------------------------------
class RWController(ABC):
    @staticmethod
    def translate_route(route_name, callback):
        routes = []
        for locale, route_path in RWMemoryI18n.all(route_name).items():
            routes.append(
                Route(
                    route_path, endpoint=callback, name="%s_%s" % (route_name, locale)
                )
            )
        return routes

    def get_routes(self):
        raise NotImplementedError

    @staticmethod
    def prepare_view_data(request, view_data=None):
        if not view_data:
            view_data = {}

        def url_for(route_name, locale=None, **path_params):
            if not locale:
                locale = request.state.i18n.locale

            url = None
            if locale:
                try:
                    url = request.url_for("%s_%s" % (route_name, locale), **path_params)
                except:
                    pass

            if not url:
                url = request.url_for(route_name, **path_params)

            return url

        view_data.update(
            {"url_for": url_for, "i18n": request.state.i18n, "config": Config}
        )

        return view_data

    def render_view(self, name, request, view_data=None):
        return HTMLResponse(
            RWView.render(name, self.prepare_view_data(request, view_data))
        )


class RWStaticFilesController(RWController):
    def __init__(self, project_dir, output_dir):
        self.project_dir = project_dir
        self.output_dir = output_dir

    def get_routes(self):
        return [
            Mount(
                self.output_dir,
                app=StaticFiles(directory=self.project_dir),
                name="static",
            )
        ]


class RWGraphQLController(RWController):
    def __init__(self, query, mutation, prefix="/api"):
        self._prefix = prefix
        self._schema = graphene.Schema(query, mutation, auto_camelcase=False)
        super().__init__()

    def get_routes(self):
        routes = [
            Route(
                self._prefix,
                GraphQLApp(schema=self._schema, executor_class=AsyncioExecutor),
                methods=["POST"],
                name="graphql",
            ),
        ]

        return routes


# --- MODELS ----------------------------------------------------------------------------------------------------
class RWMysqlModelMeta(type):
    table = None

    def __getattr__(self, item):
        return getattr(self.table, item)


class RWMysqlModel(metaclass=RWMysqlModelMeta):
    datazone = None
    table_name = None
    db = None
    _columns = []
    _filter_columns = []

    def __init_subclass__(cls):
        """used to populate the zones dictionary"""
        if not cls.datazone:
            raise Exception("Table %s must specify a zone" % cls.table_name)

        Datazones.add(cls.datazone)

        columns = [
            sqlalchemy.Column("id", sqlalchemy.Binary(16), primary_key=True),
        ] + cls.get_columns()
        cls.table = sqlalchemy.Table(cls.table_name, metadata, *columns)

    @staticmethod
    def get_columns():
        raise NotImplementedError

    @classmethod
    def get_datazone_db(cls, info):
        return info.context["request"].state.mysql[cls.datazone]


class RWMysqlHistoryModel(RWMysqlModel):
    datazone = "history"

    @staticmethod
    def get_columns():
        return [
            sqlalchemy.Column(
                "table_record_id", sqlalchemy.String(length=250), nullable=False
            ),
            sqlalchemy.Column("who", sqlalchemy.String(length=250), nullable=False),
            sqlalchemy.Column(
                "why", sqlalchemy.Enum("INSERT", "UPDATE", "DELETE"), nullable=False
            ),
            sqlalchemy.Column("what", sqlalchemy.JSON(), nullable=False),
            sqlalchemy.Column("when", sqlalchemy.DateTime(), nullable=False),
            sqlalchemy.Column("description", sqlalchemy.String(length=500)),
        ]


# --- VIEWS ----------------------------------------------------------------------------------------------------
class RWView:
    template_lookup = None

    @classmethod
    def render(cls, name, data=None):
        if not cls.template_lookup:
            cls.template_lookup = TemplateLookup(
                directories=[Config["RW_VIEWS_TEMPLATE_DIR"]]
            )

        try:
            mytemplate = cls.template_lookup.get_template(
                "%s/%s.mako" % (name, data["i18n"].locale)
            )
        except:
            mytemplate = cls.template_lookup.get_template("%s/main.mako" % name)

        return mytemplate.render(**(data or {}))
