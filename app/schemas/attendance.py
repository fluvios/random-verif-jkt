from pydantic import BaseModel

class AttendanceUpdate(BaseModel):
    attendee_id: int
    theater_id: int
    attended: bool
