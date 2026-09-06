from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = ""

    openai_api_key: str = ""
    gemini_api_key: str = ""

    mitre_attack_data_path: str = ""

    class Config:
        env_file = ".env"


settings = Settings()