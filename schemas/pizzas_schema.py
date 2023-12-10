from pydantic import BaseModel


class PizzaBase(BaseModel):
    name: str
    price: float
    img_source: str


class PizzaInDBBase(PizzaBase):
    id: int

    class Config:
        from_attributes = True


class PizzaModel(PizzaInDBBase):
    pass
