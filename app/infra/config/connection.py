from os import getenv as env

from infra.config.schemas import metadata
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class Connection:
    def __init__(self) -> None:
        self.url = f"{env('DB_NAME')}+{env('CONNECTOR')}://{env('USER')}:{env('PASSWORD')}@{env('HOST')}:{env('PORT')}/{env('DB')}"
        print(self.url)
        self.engine = create_async_engine(
            self.url, echo=True, pool_size=10, max_overflow=20
        )
        self.session_maker = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def _create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(metadata.create_all)

    async def __aenter__(self):
        await self._create_tables()
        self.session = self.session_maker()
        return self.session

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.commit()
        await self.session.close()
