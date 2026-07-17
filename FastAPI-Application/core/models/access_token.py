from collections.abc import AsyncGenerator

from core.models.base import Base
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from core.models.types import UserIdType


class AccessToken(
    Base,
    SQLAlchemyBaseAccessTokenTable[UserIdType],
):
    pass


async def get_access_token_db(
    session: AsyncSession = Depends(...),
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
