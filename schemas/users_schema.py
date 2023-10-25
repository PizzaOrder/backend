from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserBase(BaseModel):
    first_name: str
    last_name: str | None = None
    telephone: PhoneNumber

    class Config:
        from_attributes = True


class UserInDBBase(UserBase):
    id: int


class User(UserInDBBase):
    pass
