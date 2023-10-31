from pydantic import BaseModel


class PizzaBase(BaseModel):
    name: str
    price: float

    class Config:
        from_attributes = True


class PizzaInDBBase(PizzaBase):
    id: int


class PizzaModel(PizzaInDBBase):
    pass
