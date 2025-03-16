from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Blacklist(Base):
    __tablename__ = "blacklist"

    id = Column(Integer, primary_key=True, index=True)
    attendee_id = Column(Integer, ForeignKey('attendees.uid'), unique=True)
    reason = Column(String, nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    attendee = relationship("Attendee", backref="blacklist_record")
