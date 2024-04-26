from adapter.adapter import ModelAdapter
from domain.models.chat import Chat
from infra.config.connection import Connection


class ChatRepository:
    def __init__(self) -> None:
        self.connection = Connection()

    async def select_all_chats(self):
        query = f"""SELECT * FROM chat;"""
        async with self.connection as conn:
            await conn.execute(query)
            chats_raw = await conn.fetchall()
            chats = [ModelAdapter(chat, Chat).to_model() for chat in chats_raw]
            return chats

    async def select_chat_for_id(self, id: int):
        query = f"""
            SELECT * FROM chat
                WHERE id = {id};
            """
        async with self.connection as conn:
            await conn.execute(query)
            chat_raw = await conn.fetchall()
            return ModelAdapter(chat_raw, Chat).to_model()

    async def insert_chat(self):
        import datetime

        from infra.config.schemas import chat

        async with self.connection as conn:
            await conn.execute(chat.insert().values(update_at=datetime.datetime.now()))

    async def delete_chat(self, id: int):
        query = f"""
                DELETE FROM chat WHERE id = {id};
            """
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False
