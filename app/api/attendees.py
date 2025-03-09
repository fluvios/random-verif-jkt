from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.selector import select_random_attendees

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints
@app.post("/select_attendees/ofc")
def select_ofc_attendees(selection: SelectionInput, db: Session = Depends(get_db)):
    attendees = select_attendees(selection.theater_id, selection.maximum_attendees, TicketTypeEnum.OFC, db)
    return {"selected_attendees": attendees}

@app.post("/select_attendees/general")
def select_general_attendees(selection: SelectionInput, db: Session = Depends(get_db)):
    attendees = select_attendees(selection.theater_id, selection.maximum_attendees, TicketTypeEnum.GENERAL, db)
    return {"selected_attendees": attendees}

