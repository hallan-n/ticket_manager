from dotenv import load_dotenv
from fastapi import FastAPI

from app.infra.routes.ticket_router import route as ticket

load_dotenv()

app = FastAPI()

app.include_router(ticket)
