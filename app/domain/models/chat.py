from datetime import datetime

from pydantic import BaseModel


class Chat(BaseModel):
    id: int
    update_at: datetime = datetime.now()
