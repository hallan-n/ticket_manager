from os import getenv as env

from infra.config.schemas import metadata
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class Connection:
    def __init__(self) -> None:
        self.url = f"{env('DB')}+{env('CONNECTOR')}://{env('USER')}:{env('PASSWORD')}@{env('HOST')}:{env('PORT')}/{env('DB_NAME')}"
        self.engine = create_async_engine(
            self.url, echo=True, pool_size=10, max_overflow=20
        )
        self.session = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def _create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(metadata.create_all)

    async def __aenter__(self):
        await self._create_tables()
        return self.session()

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session().close()
