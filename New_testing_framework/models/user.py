from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    password: str
    login: str
    role: Optional[str] = None
