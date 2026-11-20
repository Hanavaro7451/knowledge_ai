from typing import AsyncIterator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from backend.core.config import settings

db_url = URL.create(
    drivername='postgresql+asyncpg',
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    database=settings.POSTGRES_DB,
)

engine = create_async_engine(
    url=db_url,
    echo=settings.app_debug,
    hide_parameters=True,
)

async_session_factory = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_session() -> AsyncIterator[AsyncSession]:
    db = async_session_factory()
    try:
        yield db
    finally:
        await db.close()