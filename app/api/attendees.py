from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.security import verify_token
from app.services.selector import select_ofc_attendees, select_general_attendees

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/select_attendees/ofc")
def select_ofc(theater_id: int, maximum_attendees: int, db: Session = Depends(get_db), user: str = Depends(verify_token)):
    attendees = select_ofc_attendees(db, theater_id, maximum_attendees)
    return {"selected_attendees": attendees}

@router.post("/select_attendees/general")
def select_general(theater_id: int, maximum_attendees: int, db: Session = Depends(get_db), user: str = Depends(verify_token)):
    attendees = select_general_attendees(db, theater_id, maximum_attendees)
    return {"selected_attendees": attendees}
