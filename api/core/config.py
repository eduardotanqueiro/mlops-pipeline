# api/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Default
    ENV: str = "production"
    MODEL_PATH: str = "api/models/model.pkl"
    LOG_LEVEL: str = "INFO"

    class Config:
        # Load environment variables from a .env file
        env_file = ".env"

settings = Settings()