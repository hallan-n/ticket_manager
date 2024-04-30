from fastapi import APIRouter

from app.domain.models.user import User
from app.domain.usecases.user_usecases import UserUseCases

route = APIRouter(tags=["User"])
case = UserUseCases()


@route.get("/user")
async def get_all_users(page: int, page_lenght: int):
    resp = await case.get_all_users(page, page_lenght)
    return resp


@route.get("/user/{id}")
async def get_user(id: int):
    resp = await case.get_user(id)
    return resp


@route.post("/user")
async def insert_user(user: User):
    resp = await case.insert_user(user)
    return {"Sucess": resp}


@route.put("/user")
async def update_user(user: User):
    resp = await case.update_user(user)
    return {"Sucess": resp}
