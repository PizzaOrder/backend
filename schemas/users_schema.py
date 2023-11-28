from datetime import datetime

from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserCredentials(BaseModel):
    email: EmailStr


class UserCredentialsWithCode(UserCredentials):
    verification_code: int


class UserBase(BaseModel):
    first_name: str
    last_name: str | None = None
    telephone: PhoneNumber

    class Config:
        from_attributes = True


class UserInDBBase(UserBase):
    id: int
    created_at: datetime


class UserModel(UserInDBBase):
    pass
