from adapter.adapter import ModelAdapter
from domain.models.ticket import Ticket
from infra.connection import Connection


class TicketRepository:
    def __init__(self) -> None:
        self.connection = Connection()

    async def select_all_tickets(self):
        query = f"""SELECT * FROM ticket;"""
        async with self.connection as conn:
            await conn.execute(query)
            tickets_raw = await conn.fetchall()
            tickets = [
                ModelAdapter(ticket, Ticket).to_model() for ticket in tickets_raw
            ]
            return tickets

    async def select_ticket_for_id(self, id: int):
        query = f"""
            SELECT * FROM ticket
                WHERE id = {id};
            """
        async with self.connection as conn:
            try:
                await conn.execute(query)
                ticket_raw = await conn.fetchall()
                return ModelAdapter(ticket_raw, Ticket).to_model()
            except:
                return None

    async def insert_ticket(self, ticket: Ticket):
        query = f"""
                INSERT INTO ticket
                (title,open_date,resolution_date,status,sla)
                VALUES(
                    '{ticket.title}',
                    '{ticket.open_date}',
                    '{ticket.resolution_date}',
                    '{ticket.status}',
                    {ticket.sla});
            """
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False

    async def delete_ticket(self, id: int):
        query = f"""
                DELETE FROM ticket WHERE id = {id};
            """
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False

    async def update_ticket(self, ticket: Ticket):
        query = f"""
                UPDATE ticket SET
                    title = '{ticket.title}',
                    open_date = '{ticket.open_date}',
                    resolution_date = '{ticket.resolution_date}',
                    status = '{ticket.status}',
                    sla = {ticket.sla}
                    WHERE id = {ticket.id};
            """
        async with self.connection as conn:
            try:
                await conn.execute(query)
                return True
            except:
                return False
