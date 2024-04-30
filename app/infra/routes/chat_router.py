from fastapi import APIRouter

from app.domain.usecases.chat_usecases import ChatUseCases

route = APIRouter(tags=["Chat"])
case = ChatUseCases()


@route.get("/chat")
async def select_all_chats(page: int, page_lenght: int):
    resp = await case.select_all_chats(page, page_lenght)
    return resp


@route.get("/chat/{id}")
async def select_chat_for_id(id: int):
    resp = await case.select_chat_by_id(id)
    return resp


@route.post("/chat")
async def insert_chat():
    resp = await case.insert_chat()
    return {"Sucess": resp}
