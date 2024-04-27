from adapter.adapter import ModelAdapter
from domain.models.chat import Chat
from infra.config.connection import Connection
from infra.config.schemas import chat_table


class ChatRepository:
    def __init__(self) -> None:
        self.connection = Connection()
        self.chat_table = chat_table

    async def select_all_chats(self, page: int, page_lenght: int):
        if page <= 0 or page_lenght <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")

        offset = (page - 1) * page_lenght
        query = self.chat_table.select().offset(offset).limit(page_lenght)
        async with self.connection as conn:
            try:
                result = await conn.execute(query)
                chats_raw = result.fetchall()
                chats = [ModelAdapter(chat, Chat).to_model() for chat in chats_raw]
                return chats
            except:
                return []

    async def select_chat_for_id(self, id: int):
        if id <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")
        query = self.chat_table.select().where(self.chat_table.c.id == id)

        async with self.connection as conn:
            try:
                result = await conn.execute(query)
                chats_raw = result.fetchone()
                chat = ModelAdapter(chats_raw, Chat).to_model()
                return chat
            except:
                return False

    async def insert_chat(self):
        query = self.chat_table.insert()
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False
