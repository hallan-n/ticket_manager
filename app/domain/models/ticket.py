from pydantic import BaseModel
from datetime import datetime

class Ticket(BaseModel):
    id: int
    title: str
    open_date: datetime = datetime.now()
    resolution_date: datetime = None
    status: str = None
    sla: bool = False