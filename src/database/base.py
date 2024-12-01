from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from typing import TypeVar

from src.config import config


DB_URL: str = config.sqlite.url


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


ModelType = TypeVar(
    name="ModelType",
    bound=Base
)
