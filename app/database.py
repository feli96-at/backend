from typing import Annotated

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BeforeValidator

from .config import settings

client = AsyncIOMotorClient(settings.uri)
db = client.db
PyObjectId = Annotated[str, BeforeValidator(str)]
