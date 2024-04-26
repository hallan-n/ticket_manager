# from dotenv import load_dotenv
# from fastapi import FastAPI
# from infra.routes.ticket_router import route as ticket

# load_dotenv()

# app = FastAPI()

# app.include_router(ticket)

from infra.config.connection import Connection

conn = Connection("mysql+aiomysql://root:123456@localhost/ticket_manager")


async def teste():
    async with conn as c:
        pass


import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(teste())
