from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: int
    name: str
    email: Optional[List[str]] # This means List of str is optional
    hobbies: List[str]