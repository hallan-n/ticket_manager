from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    id: int
    msg: str
    sent_at: datetime
    chat_id: int
    sender_id: int
    recipient_id: int
