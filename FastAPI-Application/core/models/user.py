# Ignore This

from .base import Base
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from .mixins.int_id_pk import IntPkMixin

class User(IntPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[str]
    bar: Mapped[str]

    __table_args__ = (UniqueConstraint("foo", "bar"),)
