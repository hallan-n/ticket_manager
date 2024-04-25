import asyncio

from domain.models.message import Message
from infra.repositories.message_repository import MessageRepository

chat = MessageRepository()
from datetime import datetime


async def rodar():
    msg = Message(
        id=1, chat_id=1, recipient_id=1, sender_id=2, sent_at=datetime.now(), msg="pica"
    )
    teste = await chat.update_message(msg)
    print(teste)


loop = asyncio.get_event_loop()
loop.run_until_complete(rodar())
