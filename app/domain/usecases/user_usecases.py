from app.domain.models.user import User
from app.infra.repositories.user_repository import UserRepository


class UserUseCases:
    def __init__(self) -> None:
        self.repo = UserRepository()

    async def get_all_users(self, page: int, page_lenght: int):
        resp = await self.repo.select_all_users(page, page_lenght)
        return resp

    async def get_user(self, id: int):
        resp = await self.repo.select_user_for_id(id)
        return resp

    async def insert_user(self, user: User):
        resp = await self.repo.insert_user(user)
        return resp

    async def update_user(self, user: User):
        resp = await self.repo.update_user(user)
        return resp
