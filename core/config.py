from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Secure DevSecOps API"
    environment: str = "dev"

    class Config:
        env_file = ".env"

settings = Settings()
