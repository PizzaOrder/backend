from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserCredentials(BaseModel):
    email: EmailStr


class UserCredentialsWithCode(UserCredentials):
    verification_code: int = Field(
        gt=99999, lt=1000000, description="Код верификации должен быть шестизначным"
    )


class UserBase(UserCredentials):
    first_name: str | None = None
    last_name: str | None = None


class UserInDBBase(UserBase):
    id: int = Field(default=None)
    created_at: datetime = Field()

    class Config:
        from_attributes = True


class ChangeUserProfile(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
