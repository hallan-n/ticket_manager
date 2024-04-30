from app.adapter.adapter import ModelAdapter
from app.adapter.dict_utils import clean_none
from app.domain.models.message import Message
from app.infra.config.connection import Connection
from app.infra.config.schemas import message_table


class MessageRepository:
    def __init__(self) -> None:
        self.connection = Connection()
        self.message_table = message_table

    async def select_all_messages(self, page: int, page_lenght: int):
        if page <= 0 or page_lenght <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")

        offset = (page - 1) * page_lenght
        query = self.message_table.select().offset(offset).limit(page_lenght)

        async with self.connection as conn:
            try:
                result = await conn.execute(query)
                messages_raw = result.fetchall()
                messages = [
                    ModelAdapter(msg, Message).to_model() for msg in messages_raw
                ]
                return messages
            except Exception as e:
                raise e

    async def select_message_by_id(self, id: int):
        if id <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")
        query = self.message_table.select().where(self.message_table.c.id == id)

        async with self.connection as conn:
            try:
                result = await conn.execute(query)
                message_raw = result.fetchone()
                message = ModelAdapter(message_raw, Message).to_model()
                return message
            except:
                return {}

    async def insert_message(self, message: Message):
        data = clean_none(message.model_dump())
        query = self.message_table.insert().values(**data)
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False
