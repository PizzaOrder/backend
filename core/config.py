from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    url: str = "postgresql+psycopg2://admin:root@localhost/PizzaOrder"


class Settings(BaseSettings):
    db: DBSettings = DBSettings()


settings = Settings()
