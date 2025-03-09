from pydantic import BaseModel
from typing import Optional

class AttendeeBase(BaseModel):
    name: str
    favorite_member: Optional[str] = None
    address: Optional[str] = None

class AttendeeCreate(AttendeeBase):
    pass

class AttendeeResponse(AttendeeBase):
    uid: int

    class Config:
        orm_mode = True
