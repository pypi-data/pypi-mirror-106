from starlette.middleware.base import BaseHTTPMiddleware


class AclMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.identity = {}  # TODO
        return await call_next(request)
