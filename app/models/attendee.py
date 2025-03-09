from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Attendee(Base):
    __tablename__ = "attendees"

    uid = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    favorite_member = Column(String, nullable=True)
    address = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)
    city = Column(String, nullable=True)
    province = Column(String, nullable=True)
