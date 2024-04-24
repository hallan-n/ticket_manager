import asyncio
import os

import aiomysql


class Connection:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.config = {
            "host": os.getenv("HOST"),
            "port": int(os.getenv("PORT")),
            "user": os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
            "db": os.getenv("DB"),
            "loop": self.loop,
        }

    async def _connect(self):
        self.conn = await aiomysql.connect(**self.config)

    async def __aenter__(self):
        await self._connect()
        self.cursor = await self.conn.cursor()
        return self.cursor

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.conn.commit()
        await self.cursor.close()
        self.conn.close()
