from adapter.adapter import ModelAdapter
from domain.models.user import User
from infra.config.connection import Connection


class UserRepository:
    def __init__(self) -> None:
        self.connection = Connection()

    async def select_all_users(self):
        query = f"""SELECT * FROM user;"""
        async with self.connection as conn:
            await conn.execute(query)
            users_raw = await conn.fetchall()
            users = [ModelAdapter(user, User).to_model() for user in users_raw]
            return users

    async def select_user_for_id(self, id: int):
        query = f"""
            SELECT * FROM user
                WHERE id = {id};
            """
        async with self.connection as conn:
            await conn.execute(query)
            user_raw = await conn.fetchall()
            return ModelAdapter(user_raw, User).to_model()

    async def insert_user(self, user: User):
        query = f"""
                INSERT INTO user
                (name,login,password)
                VALUES(
                    '{user.name}',
                    '{user.login}',
                    '{user.password}');
            """
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False

    async def update_user(self, user: User):
        query = f"""
                UPDATE user SET
                    name = '{user.name}',
                    login = '{user.login}',
                    password = '{user.password}'
                    WHERE id = {user.id};
            """
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False
