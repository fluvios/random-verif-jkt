from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    attendee_id = Column(Integer, ForeignKey('attendees.uid'))
    theater_id = Column(Integer, ForeignKey('theaters.id'))
    attended = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    attendee = relationship("Attendee", backref="attendance_records")
    theater = relationship("Theater", backref="attendance_records")
