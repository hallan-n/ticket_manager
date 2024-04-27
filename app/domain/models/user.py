from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    name: str
    login: str
    password: str
    create_at: datetime = None
    update_at: datetime = None
