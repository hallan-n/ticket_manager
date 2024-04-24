# from dotenv import load_dotenv
# load_dotenv()
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def hello_world():
#     return {"msg": "Rodando"}

# import asyncio
# from infra.repositories.chat_repository import ChatRepository
# chat = ChatRepository()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(chat.insert_chat())
# loop.run_until_complete(chat.select_all_chats())
# loop.run_until_complete(chat.delete_chat_for_id(3))
