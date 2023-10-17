from pydantic import BaseModel


class PizzaBase(BaseModel):
    pizza_id: int
    name: str
    price: float

    class Config:
        from_attributes = True
