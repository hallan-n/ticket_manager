from dotenv import load_dotenv

# from fastapi import FastAPI
# from infra.routes.ticket_router import route as ticket

load_dotenv()

# app = FastAPI()

# app.include_router(ticket)

from infra.config.connection import Connection
from infra.repositories.chat_repository import ChatRepository

conn = Connection()
chat = ChatRepository()


async def teste():
    await chat.insert_chat()


import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(teste())
