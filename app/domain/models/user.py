from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    login: str
    password: str