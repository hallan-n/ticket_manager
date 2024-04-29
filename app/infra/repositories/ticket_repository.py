from app.adapter.adapter import ModelAdapter
from app.adapter.dict_utils import clean_none
from app.domain.models.ticket import Ticket
from app.infra.config.connection import Connection
from app.infra.config.schemas import ticket_table


class TicketRepository:
    def __init__(self) -> None:
        self.connection = Connection()
        self.ticket_table = ticket_table

    async def select_all_tickets(self, page: int, page_lenght: int):
        if page <= 0 or page_lenght <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")

        offset = (page - 1) * page_lenght
        query = self.ticket_table.select().offset(offset).limit(page_lenght)
        async with self.connection as conn:
            try:
                result = await conn.execute(query)
                tickets_raw = result.fetchall()
                tickets = [
                    ModelAdapter(ticket, Ticket).to_model() for ticket in tickets_raw
                ]
                return tickets
            except:
                return []

    async def select_ticket_for_id(self, id: int):
        if id <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")
        query = self.ticket_table.select().where(self.ticket_table.c.id == id)

        async with self.connection as conn:
            try:
                result = await conn.execute(query)
                ticket_raw = result.fetchone()
                ticket = ModelAdapter(ticket_raw, Ticket).to_model()
                return ticket
            except:
                return {}

    async def insert_ticket(self, ticket: Ticket):
        data = clean_none(ticket.model_dump())
        query = self.ticket_table.insert().values(**data)
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False

    async def update_ticket(self, ticket: Ticket):
        data = clean_none(ticket.model_dump())

        query = (
            self.ticket_table.update()
            .values(**data)
            .where(self.ticket_table.c.id == ticket.id)
        )

        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False

    async def delete_ticket(self, id: int):
        if id <= 0:
            raise ValueError("Os parâmetro devem ter valores positivos")

        query = self.ticket_table.delete().where(self.ticket_table.c.id == id)

        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False
