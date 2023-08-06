from starlette.middleware.base import BaseHTTPMiddleware
from red_warden.config import Logger, Datazones, Backends


class DbMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        datazone_user = request.state.identity.get("datazone_user", "GLOBAL")

        for backend in ["mysql", "mongodb", "redis"]:
            state_backend = getattr(request.state, backend, None)
            if not state_backend:
                setattr(request.state, backend, {})
                state_backend = getattr(request.state, backend)

            for datazone_name in Datazones.get_names():
                datazone_config = Datazones.get_configuration(
                    datazone_name, datazone_user
                )
                datazone_backend = datazone_config.get(backend, None)
                if datazone_backend:
                    state_backend[datazone_name] = Backends.get(
                        datazone_backend["backend"],
                        additional_params=datazone_backend.get("params", None),
                    )

        for backend in ["mysql", "mongodb", "redis"]:
            state_backend = getattr(request.state, backend)
            for _, db in state_backend.items():
                try:
                    await db.connect()
                except Exception as ex:
                    Logger.error(ex)

        results = await call_next(request)

        for backend in ["mysql", "mongodb", "redis"]:
            state_backend = getattr(request.state, backend)
            for _, db in state_backend.items():
                try:
                    if db.is_connected:
                        await db.disconnect()
                except Exception as ex:
                    Logger.error(ex)

        return results
