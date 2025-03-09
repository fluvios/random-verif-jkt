from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.enums.ticket import TicketTypeEnum, StatusEnum

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    ticket_buy_date = Column(DateTime)
    theater_id = Column(Integer, ForeignKey('theaters.id'))
    user_id = Column(Integer, ForeignKey('attendees.uid'))
    status = Column(Enum(StatusEnum))
    show_type = Column(String)
    ticket_type = Column(Enum(TicketTypeEnum))

    theater = relationship("Theater")
    attendee = relationship("Attendee")
