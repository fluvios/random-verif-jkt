from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.enums.ticket import TicketTypeEnum

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    attendee_id = Column(Integer, ForeignKey('attendees.uid'))
    theater_id = Column(Integer, ForeignKey('theaters.id'))
    application_id = Column(Integer, ForeignKey('applications.id'))
    issued_date = Column(DateTime, nullable=False)
    ticket_type = Column(Enum(TicketTypeEnum), nullable=False)

    attendee = relationship("Attendee", backref="tickets")
    theater = relationship("Theater", backref="tickets")
    application = relationship("Application")
