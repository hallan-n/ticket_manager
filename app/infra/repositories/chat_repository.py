from adapter.chat_adapter import ChatAdapter
from infra.connection import Connection


class ChatRepository:
    def __init__(self) -> None:
        self.connection = Connection()

    async def select_all_chats(self):
        query = f"""SELECT * FROM chat;"""
        async with self.connection as conn:
            await conn.execute(query)
            chats_raw = await conn.fetchall()
            chats = [ChatAdapter(chat).to_model() for chat in chats_raw]
            return chats

    async def select_chat_for_id(self, id: int):
        query = f"""
            SELECT * FROM chat
                WHERE id = {id};
            """
        async with self.connection as conn:
            await conn.execute(query)
            chat = await conn.fetchall()
            return ChatAdapter(chat).to_model()

    async def insert_chat(self):
        query = f"""
                INSERT INTO chat(update_at) VALUES(now());
            """
        async with self.connection as conn:
            await conn.execute(query)

    async def delete_chat(self, id: int):
        query = f"""
                DELETE FROM chat WHERE id = {id};
            """
        async with self.connection as conn:
            await conn.execute(query)
