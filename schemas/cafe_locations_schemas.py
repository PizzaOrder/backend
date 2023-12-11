from pydantic import BaseModel

from schemas.cities_schema import CityModel


class CafeLocationBase(BaseModel):
    city_id: int
    street: str
    house: str

    class Config:
        from_attributes = True


class CafeLocationInDBBase(CafeLocationBase):
    id: int


class CafeLocationModel(CafeLocationInDBBase):
    pass


class CafeLocationWithCity(CafeLocationModel):
    city: list[CityModel] | CityModel
