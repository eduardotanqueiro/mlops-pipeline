# api/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Default
    ENV: str = "production"
    MODEL_PATH: str = "ckpt/model.pkl"
    LOG_LEVEL: str = "INFO"

    class Config:
        # Load environment variables from a .env file
        env_file = ".env"

settings = Settings()