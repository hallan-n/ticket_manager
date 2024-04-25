from datetime import datetime

from pydantic import BaseModel


class Chat(BaseModel):
    id: int = None
    update_at: datetime = datetime.now()
