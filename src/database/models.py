from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )
    full_name: Mapped[str]
    phone: Mapped[str]
    address: Mapped[str]

    comments: Mapped[list["Comment"]] = relationship(
        argument="Comment",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )
    text: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(
        argument="User",
        back_populates="comments"
    )
