from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCredentials(BaseModel):
    email: EmailStr


class UserCredentialsWithCode(UserCredentials):
    verification_code: int


class UserBase(BaseModel):
    first_name: str

    class Config:
        from_attributes = True


class UserInDBBase(UserBase):
    id: int
    created_at: datetime


class UserModel(UserInDBBase):
    pass
