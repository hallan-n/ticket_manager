from app.domain.models.ticket import Ticket
from app.infra.repositories.chat_repository import ChatRepository


class ChatUseCases:
    def __init__(self) -> None:
        self.repo = ChatRepository()

    async def select_all_chats(self, page: int, page_lenght: int):
        resp = await self.repo.select_all_chats(page, page_lenght)
        return resp

    async def select_chat_by_id(self, id: int):
        resp = await self.repo.select_chat_by_id(id)
        return resp

    async def insert_chat(self):
        resp = await self.repo.insert_chat()
        return resp
