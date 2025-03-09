from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from .theater_member import theater_member_association

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    theaters = relationship(
        "Theater",
        secondary=theater_member_association,
        back_populates="members"
    )
