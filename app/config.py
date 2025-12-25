from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

    model_config = {
        "env_file": ".env",  # <-- load variables from .env automatically
        "extra": "ignore"
    }

settings = Settings()

