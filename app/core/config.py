import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./attendees.db"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "jkt482025")
    APP_NAME: str = "Theater Verifier"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
