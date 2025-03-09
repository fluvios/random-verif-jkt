import pandas as pd
from sqlalchemy.orm import Session
from app.models.attendee import Attendee

def import_attendees(file, db: Session):
    try:
        df = pd.read_excel(file) if file.filename.endswith('.xlsx') else pd.read_csv(file)
    except Exception as e:
        raise ValueError(f"Failed to read file: {e}")

    required_columns = ['name', 'favorite_member', 'address', 'postal_code', 'city', 'province']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"File must contain columns: {required_columns}")

    attendees_added = 0

    for _, row in df.iterrows():
        attendee = Attendee(
            name=row['name'],
            favorite_member=row.get('favorite_member'),
            address=row.get('address'),
            postal_code=row.get('postal_code'),
            city=row.get('city'),
            province=row.get('province')
        )
        db.add(attendee)
        attendees_added += 1

    db.commit()
    return attendees_added
