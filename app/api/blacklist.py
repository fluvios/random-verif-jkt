from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.security import verify_token
from app.models.blacklist import Blacklist
from app.schemas.blacklist import BlacklistCreate, BlacklistResponse
from typing import List
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add attendee to blacklist
@router.post("/blacklist", response_model=BlacklistResponse, dependencies=[Depends(verify_token)])
def add_to_blacklist(blacklist: BlacklistCreate, db: Session = Depends(get_db)):
    existing = db.query(Blacklist).filter(Blacklist.attendee_id == blacklist.attendee_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Attendee already blacklisted.")

    db_blacklist = Blacklist(
        attendee_id=blacklist.attendee_id,
        reason=blacklist.reason,
        start_date=blacklist.start_date or datetime.utcnow(),
        end_date=blacklist.end_date
    )
    db.add(db_blacklist)
    db.commit()
    db.refresh(db_blacklist)
    return db_blacklist

# Remove attendee from blacklist
@router.delete("/blacklist/{attendee_id}", dependencies=[Depends(verify_token)])
def remove_from_blacklist(attendee_id: int, db: Session = Depends(get_db)):
    record = db.query(Blacklist).filter(Blacklist.attendee_id == attendee_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Blacklist record not found.")

    db.delete(record)
    db.commit()
    return {"message": "Attendee removed from blacklist."}

# View all blacklisted attendees
@router.get("/blacklist", response_model=List[BlacklistResponse], dependencies=[Depends(verify_token)])
def get_blacklist(db: Session = Depends(get_db)):
    return db.query(Blacklist).all()

# Check attendee blacklist status
@router.get("/blacklist/{attendee_id}", response_model=BlacklistResponse, dependencies=[Depends(verify_token)])
def check_blacklist(attendee_id: int, db: Session = Depends(get_db)):
    record = db.query(Blacklist).filter(Blacklist.attendee_id == attendee_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Attendee is not blacklisted.")
    return record
