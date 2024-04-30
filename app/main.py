from dotenv import load_dotenv
from fastapi import FastAPI

from app.infra.routes.chat_router import route as chat
from app.infra.routes.message_router import route as message
from app.infra.routes.ticket_router import route as ticket
from app.infra.routes.user_router import route as user

load_dotenv()

app = FastAPI()

app.include_router(ticket)
app.include_router(user)
app.include_router(chat)
app.include_router(message)
