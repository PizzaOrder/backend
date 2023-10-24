from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    url: str = "postgresql://admin@localhost:5432/PizzaOrder"


class Settings(BaseSettings):
    db: DBSettings = DBSettings()


settings = Settings()
