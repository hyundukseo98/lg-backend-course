from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mysql+pymysql://username:password@localhost:3306/rcmd_practice"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    port: int = 8080

    class Config:
        env_file = ".env"

settings = Settings()