from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./fraud.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
