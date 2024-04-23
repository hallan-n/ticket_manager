from datetime import datetime

from pydantic import BaseModel


class Ticket(BaseModel):
    id: int
    title: str
    open_date: datetime = datetime.now()
    resolution_date: datetime = None
    status: str = None
    sla: bool = False
