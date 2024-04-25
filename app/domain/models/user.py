from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    name: str
    login: str
    password: str
