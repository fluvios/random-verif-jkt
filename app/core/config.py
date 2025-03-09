import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./attendees.db"
    APP_NAME: str = "Random Attendee Selector"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
