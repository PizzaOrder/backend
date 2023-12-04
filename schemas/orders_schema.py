from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    user_id: int
    promo_id: int = None
    total_cost: float
    order_date: datetime
    order_status: str

    class Config:
        from_attributes = True


class OrderInDBBase(OrderBase):
    id: int


class OrderModel(OrderInDBBase):
    pass
