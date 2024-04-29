from fastapi import APIRouter

from app.domain.models.ticket import Ticket
from app.domain.usecases.ticket_usecases import TicketUseCases

route = APIRouter(tags=["Ticket"])
repo = TicketUseCases()


@route.post("/ticket")
async def open_ticket(ticket: Ticket):
    """Crie um chamado"""
    resp = await repo.open_ticket(ticket)
    return {"Sucess": resp}


@route.delete("/ticket/{id}")
async def close_ticket(id: int):
    resp = await repo.close_ticket(id)
    return {"Sucess": resp}


@route.put("/ticket")
async def att_ticket(ticket: Ticket):
    resp = await repo.att_ticket(ticket)
    return {"Sucess": resp}


@route.get("/ticket/{id}")
async def read_ticket(id: int):
    resp = await repo.read_ticket(id)
    return resp


@route.get("/ticket")
async def read_tickets(page: int, lenght: int):
    resp = await repo.read_tickets(page, lenght)
    return resp
