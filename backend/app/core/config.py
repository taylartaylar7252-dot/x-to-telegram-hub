from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_ID: int = 12345
    API_HASH: str = "default"
    BOT_TOKEN: str = "default"
    DATABASE_URL: str = "sqlite+aiosqlite:///./app.db"
    SECRET_KEY: str = "supersecret"
    PLAN: str = "starter"

    class Config:
        env_file = ".env"

settings = Settings()
