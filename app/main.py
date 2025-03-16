from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.attendees import router as attendees_router
from app.api.importer import router as importer_router
from app.api.attendance import router as attendance_router
from app.api.blacklist import router as blacklist_router  # New blacklist routes

app = FastAPI()

app.include_router(auth_router, prefix="/api")
app.include_router(attendees_router, prefix="/api")
app.include_router(importer_router, prefix="/api")
app.include_router(attendance_router, prefix="/api")
app.include_router(blacklist_router, prefix="/api")  # Include blacklist endpoints
