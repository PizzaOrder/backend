from pydantic import BaseModel


class PizzaBase(BaseModel):
    id: int
    name: str
    price: float
