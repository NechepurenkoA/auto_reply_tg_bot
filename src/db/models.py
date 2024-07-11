import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base


class TelegramUser(Base):
    __tablename__ = "telegram_users"

    chat_id: Mapped[int] = mapped_column(
        "tg_chat_id", sa.BigInteger, unique=True, nullable=False
    )
