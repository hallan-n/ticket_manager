from domain.models.message import Message
from infra.connection import Connection


class MessageRepository:
    def __init__(self) -> None:
        self.connection = Connection()

    async def select_all_messages(self):
        query = f"""SELECT * FROM message;"""
        async with self.connection as conn:
            await conn.execute(query)

    async def select_message_for_id(self, id: int):
        query = f"""
            SELECT * FROM message
                WHERE id = {id};
            """
        async with self.connection as conn:
            await conn.execute(query)

    async def insert_messaget(self, message: Message):
        query = f"""
                INSERT INTO message
                (msg,sent_at,chat_id,sender_id,recipient_id)
                VALUES(
                    {message.msg},{message.sent_at},{message.chat_id},
                    {message.sender_id},{message.recipient_id});
            """
        async with self.connection as conn:
            await conn.execute(query)

    async def delete_message(self, id: int):
        query = f"""
                DELETE FROM message WHERE id = {id};
            """
        async with self.connection as conn:
            await conn.execute(query)

    async def update_message(self, message: Message):
        query = f"""
                UPDATE message SET
                    msg = {message.msg}
                    sent_at = {message.sent_at}
                    chat_id = {message.chat_id}
                    sender_id = {message.sender_id}
                    recipient_id = {message.recipient_id}
                    WHERE id = {message.id};
            """
        async with self.connection as conn:
            await conn.execute(query)
