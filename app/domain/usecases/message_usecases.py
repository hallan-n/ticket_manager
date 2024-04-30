from app.domain.models.message import Message
from app.infra.repositories.message_repository import MessageRepository


class MessageUseCases:
    def __init__(self) -> None:
        self.repo = MessageRepository()

    async def select_all_messages(self, page: int, page_lenght: int):
        resp = await self.repo.select_all_messages(page, page_lenght)
        return resp

    async def select_message_by_id(self, id: int):
        resp = await self.repo.select_message_by_id(id)
        return resp

    async def insert_message(self, message: Message):
        resp = await self.repo.insert_message(message)
        return resp
