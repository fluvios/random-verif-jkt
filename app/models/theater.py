from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
from enums.theater import SpecialEventEnum
from .theater_member import theater_member_association

class Theater(Base):
    __tablename__ = "theaters"

    id = Column(Integer, primary_key=True, index=True)
    show_name = Column(String, nullable=False)
    show_date = Column(DateTime, nullable=False)
    special_event = Column(Enum(SpecialEventEnum), nullable=False, default=SpecialEventEnum.NONE)

    members = relationship(
        "Member",
        secondary=theater_member_association,
        back_populates="theaters"
    )
