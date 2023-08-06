import json
from typing import Any, Optional
from cryptography.fernet import Fernet
from red_warden.config import Backends
from red_warden.helpers import CustomJsonEncoder


class AioRedisSessionBackend:
    def __init__(self, redis_backend_name, secret):
        self.redis = Backends.get(redis_backend_name)
        self.fernet = Fernet(str(secret))

    async def check_connection(self):
        if not self.redis.is_connected:
            await self.redis.connect()

    async def get(self, key: str) -> Optional[dict]:
        await self.check_connection()
        encrypted = await self.redis.get(key)
        if not encrypted:
            return None

        return json.loads(self.fernet.decrypt(encrypted))

    async def set(
        self, key: str, value: dict, exp: Optional[int] = None
    ) -> Optional[str]:  # pragma: no cover
        await self.check_connection()
        s = json.dumps(value, cls=CustomJsonEncoder)
        return await self.redis.set(key, self.fernet.encrypt(s.encode()), expire=exp)

    async def delete(self, key: str) -> Any:
        await self.check_connection()
        return await self.redis.delete(key)
