from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.security import verify_token
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/update_attendance", dependencies=[Depends(verify_token)])
def update_attendance(data: AttendanceUpdate, db: Session = Depends(get_db)):
    attendance_record = db.query(Attendance).filter_by(
        attendee_id=data.attendee_id,
        theater_id=data.theater_id
    ).first()

    if attendance_record:
        attendance_record.attended = data.attended
    else:
        attendance_record = Attendance(
            attendee_id=data.attendee_id,
            theater_id=data.theater_id,
            attended=data.attended
        )
        db.add(attendance_record)

    db.commit()
    return {"message": "Attendance updated successfully"}
