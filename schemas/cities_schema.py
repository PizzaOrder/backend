from pydantic import BaseModel


class City(BaseModel):
    city: str


class CityInDBBase(City):
    id: int

    class Config:
        from_attributes = True


class CityModel(CityInDBBase):
    pass
