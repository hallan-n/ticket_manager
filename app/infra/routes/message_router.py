from fastapi import APIRouter

from app.domain.models.message import Message
from app.domain.usecases.message_usecases import MessageUseCases

route = APIRouter(tags=["Message"])
case = MessageUseCases()


@route.get("/message")
async def select_all_messages(page: int, page_lenght: int):
    resp = await case.select_all_messages(page, page_lenght)
    return resp


@route.get("/message/{id}")
async def select_message_by_id(id: int):
    resp = await case.select_message_by_id(id)
    return resp


@route.post("/message")
async def insert_message(message: Message):
    resp = await case.insert_message(message)
    return {"Sucess": resp}
