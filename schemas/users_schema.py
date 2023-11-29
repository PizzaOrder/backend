from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCredentials(BaseModel):
    email: EmailStr


class UserCredentialsWithCode(UserCredentials):
    verification_code: int


class UserBase(UserCredentials):
    first_name: str
    last_name: str | None = None

    class Config:
        from_attributes = True


class UserInDBBase(UserBase):
    id: int
    created_at: datetime
