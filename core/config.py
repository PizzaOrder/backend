from pydantic import BaseModel, EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    url: str


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    model_config = SettingsConfigDict(env_file="../.env")

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    PGADMIN_MAIL: EmailStr
    PGADMIN_PW: str

    def __init__(self):
        super().__init__()
        self.db.url = (
            f"postgresql://{self.POSTGRES_USER}@localhost:5432/{self.POSTGRES_DB}"
        )


settings = Settings()
