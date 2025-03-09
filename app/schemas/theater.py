from pydantic import BaseModel
from datetime import datetime
from typing import List
from .member import MemberResponse

class TheaterBase(BaseModel):
    show_name: str
    show_date: datetime

class TheaterCreate(TheaterBase):
    member_ids: List[int]

class TheaterResponse(TheaterBase):
    id: int
    members: List[MemberResponse]

    class Config:
        orm_mode = True
