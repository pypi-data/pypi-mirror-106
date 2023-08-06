import asyncio
from starlette.applications import Starlette
from red_warden.config import Config, Logger, Engines, Middlewares
from red_warden.mvc import RWGraphQLController, RWStaticFilesController
from red_warden.graphql import (
    create_query_container,
    create_mutation_container,
)

__version__ = '0.1.0'

_routes = []


class RedWarden:
    _app = None
    _controllers = []

    def __init__(self):
        Logger.info("RedWarden %s" % Config["RW_MODULE_NAME"])

    def add_controllers(self, controllers):
        if not isinstance(controllers, list):
            controllers = [controllers]

        self._controllers += controllers

    def setup_static_files(self, project_dir, output_dir):
        self.add_controllers(RWStaticFilesController(project_dir, output_dir))

    def setup_graphql(self, queries, mutations, prefix="/api"):
        self.add_controllers(
            RWGraphQLController(
                create_query_container(queries),
                create_mutation_container(mutations),
                prefix,
            )
        )

    @staticmethod
    def handle_exception(loop, context):
        # context["message"] will always be there; but context["exception"] may not
        msg = context.get("exception", context["message"])
        Logger.error(f"Asyncio loop exception: {msg}")

    def start(self):
        routes = []
        for controller in self._controllers:
            routes += controller.get_routes()

        self._app = Starlette(
            routes=routes,
            middleware=Middlewares.get_all(),
            on_startup=[self.on_startup],
            on_shutdown=[self.on_shutdown],
            debug=Config["RW_MODULE_DEBUG"],
        )

        asyncio.get_event_loop().set_exception_handler(self.handle_exception)
        return self._app

    def on_startup(self):
        for name, engine in Engines.get_all().items():
            asyncio.create_task(engine.run())

    async def on_shutdown(self):
        for name, engine in Engines.get_all().items():
            await engine.stop()
