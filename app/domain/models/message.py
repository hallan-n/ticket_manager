from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    id: int = None
    msg: str
    sent_at: datetime = None
    chat_id: int
    sender_id: int
    recipient_id: int
