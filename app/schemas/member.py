from pydantic import BaseModel

class MemberBase(BaseModel):
    name: str

class MemberCreate(MemberBase):
    pass

class MemberResponse(MemberBase):
    id: int

    class Config:
        orm_mode = True
