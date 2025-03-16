from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BlacklistBase(BaseModel):
    attendee_id: int
    reason: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class BlacklistCreate(BlacklistBase):
    pass

class BlacklistResponse(BlacklistBase):
    id: int

    class Config:
        orm_mode = True
