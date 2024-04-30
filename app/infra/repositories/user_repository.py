from app.adapter.adapter import ModelAdapter
from app.adapter.dict_utils import clean_none
from app.domain.models.user import User
from app.infra.config.connection import Connection
from app.infra.config.schemas import user_table


class UserRepository:
    def __init__(self) -> None:
        self.connection = Connection()
        self.user_table = user_table

    async def select_all_users(self, page: int, page_lenght: int):
        if page <= 0 or page_lenght <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")

        offset = (page - 1) * page_lenght
        query = self.user_table.select().offset(offset).limit(page_lenght)
        async with self.connection as conn:
            try:
                result = await conn.execute(query)
                users_raw = result.fetchall()
                users = [ModelAdapter(user, User).to_model() for user in users_raw]
                return users
            except:
                return []

    async def select_user_for_id(self, id: int):
        if id <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")
        query = self.user_table.select().where(self.user_table.c.id == id)

        async with self.connection as conn:
            try:
                result = await conn.execute(query)
                user_raw = result.fetchone()
                user = ModelAdapter(user_raw, User).to_model()
                return user
            except:
                return {}

    async def insert_user(self, user: User):
        data = clean_none(user.model_dump())
        query = self.user_table.insert().values(**data)
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False

    async def update_user(self, user: User):
        data = clean_none(user.model_dump())

        query = (
            self.user_table.update()
            .values(**data)
            .where(self.user_table.c.id == user.id)
        )

        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False
