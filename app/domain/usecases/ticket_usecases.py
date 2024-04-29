from app.domain.models.ticket import Ticket
from app.infra.repositories.ticket_repository import TicketRepository


class TicketUseCases:
    def __init__(self) -> None:
        self.repo = TicketRepository()

    async def open_ticket(self, ticket: Ticket):
        resp = await self.repo.insert_ticket(ticket)
        return resp

    async def close_ticket(self, id: int):
        resp = await self.repo.delete_ticket(id)
        return resp

    async def att_ticket(self, ticket: Ticket):
        resp = await self.repo.update_ticket(ticket)
        return resp

    async def read_ticket(self, id: int):
        resp = await self.repo.select_ticket_for_id(id)
        return resp

    async def read_tickets(self, page: int, lenght: int):
        resp = await self.repo.select_all_tickets(page, lenght)
        return resp
