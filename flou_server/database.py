from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from flou_server import config, utils

logger = utils.AppLogger.__call__().get_logger()

engine = create_async_engine(
    config.get_settings().database_url,
    future=True,
    echo=True,
)

# expire_on_commit=False will prevent attributes from being expired after commit.
AsyncSessionFactory = sessionmaker(
    engine, autoflush=False, expire_on_commit=False, class_=AsyncSession
)


# Dependency
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionFactory() as session:
        logger.debug(f"ASYNC Pool: {engine.pool.status()}")
        yield session
