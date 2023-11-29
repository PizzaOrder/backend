from pydantic_settings import BaseSettings, SettingsConfigDict


# mypy: disable-error-code="call-arg"
class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    SENDER_EMAIL: str
    SENDER_PASSWORD: str

    SECRET_KEY_JWT: str
    ALGORITHM: str

    @property
    def database_dsn_psycopg2(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def email_sending(self):
        return self.SENDER_EMAIL, self.SENDER_PASSWORD, self.SENDER_EMAIL

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
