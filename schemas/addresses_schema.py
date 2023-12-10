from pydantic import BaseModel


class AddressBase(BaseModel):
    user_id: int
    city: str
    street: str
    house: str
    floor: int | None = None
    apartment: str | None = None

    class Config:
        from_attributes = True


class AddressInDBBase(AddressBase):
    id: int


class AddressesModel(AddressInDBBase):
    pass
