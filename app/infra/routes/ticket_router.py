from fastapi import APIRouter

from app.domain.models.ticket import Ticket
from app.domain.usecases.ticket_usecases import TicketUseCases

route = APIRouter(tags=["Ticket"])
case = TicketUseCases()


@route.post("/ticket")
async def open_ticket(ticket: Ticket):
    """Crie um chamado"""
    resp = await case.open_ticket(ticket)
    return {"Sucess": resp}


@route.delete("/ticket/{id}")
async def close_ticket(id: int):
    """Deleta um chamado"""
    resp = await case.close_ticket(id)
    return {"Sucess": resp}


@route.put("/ticket")
async def att_ticket(ticket: Ticket):
    """Atualiza um chamado"""
    resp = await case.att_ticket(ticket)
    return {"Sucess": resp}


@route.get("/ticket/{id}")
async def read_ticket(id: int):
    """Ler um chamado"""
    resp = await case.read_ticket(id)
    return resp


@route.get("/ticket")
async def read_tickets(page: int, lenght: int):
    """Ler todos os chamados"""
    resp = await case.read_tickets(page, lenght)
    return resp
