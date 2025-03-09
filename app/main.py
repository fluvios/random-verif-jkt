from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.attendees import router as attendees_router

app = FastAPI()

app.include_router(auth_router, prefix="/api")
app.include_router(attendees_router, prefix="/api")
