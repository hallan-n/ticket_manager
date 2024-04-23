from pydantic import BaseModel
from datetime import datetime



class Chat(BaseModel):
  id: int
  update_at: datetime = datetime.now()