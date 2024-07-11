from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from src.db.config import settings


class PreBase:

    id: Mapped[int] = mapped_column(primary_key=True)


Base = declarative_base(cls=PreBase)
engine = create_async_engine(settings.asyncpg_url.unicode_string(), echo=True)


AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
