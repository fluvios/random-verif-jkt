from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base

theater_member_association = Table(
    "theater_member",
    Base.metadata,
    Column("theater_id", Integer, ForeignKey("theaters.id"), primary_key=True),
    Column("member_id", Integer, ForeignKey("members.id"), primary_key=True),
    Column("is_birthday", Boolean, default=False)
)
