from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Attendee(Base):
    __tablename__ = "attendees"

    uid = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    favorite_member = Column(String, nullable=True)
    address = Column(String, nullable=True)
