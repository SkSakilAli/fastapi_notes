from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Table, Column, Integer, Boolean, DateTime
from ..db.config import SessionLocal, engine
import datetime as dt


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False)


class RefreshToken(Base):
    __tablename__ = "refreshtoken"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped["User"] = mapped_column(
        ForeignKey("user.id", ondelete="cascade"), nullable=False, unique=False
    )
    token: Mapped[str] = mapped_column(String)
    expires_at: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True))
    revoked: Mapped[bool] = mapped_column(Boolean, default=True)


def create_tables():
    Base.metadata.create_all(engine)


# create_tables()
