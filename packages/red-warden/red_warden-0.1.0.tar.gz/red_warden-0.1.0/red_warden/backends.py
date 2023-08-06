import asyncio
import aioredis
import databases
from aioredis import ConnectionForcedCloseError, ConnectionClosedError
from red_warden.config import Config, Logger


class RWMysqlBackend(databases.Database):
    def __init__(self, endpoint, params):
        username = params.get("username", None)
        password = params.get("password", None)
        url = "mysql://"
        if username or password:
            url += "%s:%s" % (username, password)

        url += "@%s" % endpoint

        db_name = params.get("db_name", None)
        if db_name:
            url += "/%s" % db_name

        self.server_code = params.get("server_code", "0")
        super().__init__(url, echo=Config["RW_MODULE_DEBUG"])

    async def get_uuid(self):
        # TODO we need a transaction here
        uuid = await self.fetch_val("SELECT UUID() as uuid")
        if self.server_code is not None:
            uuid = uuid[0:24] + str(self.server_code).zfill(4) + uuid[28:]

        uuid_rev = uuid[24:] + uuid[19:23] + uuid[14:18] + uuid[9:13] + uuid[:8]
        return bytes(bytearray.fromhex(uuid_rev))


class RWRedisBackend:
    _redis = None

    def __init__(self, endpoint, params):
        self._url = "redis://%s/%s" % (endpoint, params.get("db", 0))

    async def connect(self):
        while True:
            try:
                self._redis = await aioredis.create_redis(self._url, encoding="utf-8")
                break
            except (
                ConnectionForcedCloseError,
                ConnectionClosedError,
                ConnectionRefusedError,
            ) as ex:
                Logger.error(ex)
                await asyncio.sleep(1)

    async def disconnect(self):
        if self._redis:
            self._redis.close()
            await self._redis.wait_closed()
            self._redis = None

    def __getattr__(self, item):
        if not self._redis:
            raise Exception("Redis is not connected")

        return getattr(self._redis, item)
