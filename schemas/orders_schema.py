from datetime import datetime

from pydantic import BaseModel

from schemas.order_items_schema import (
    OrderItemInDBBase,
)


class OrderBase(BaseModel):
    user_id: int
    promo_id: int | None = None
    total_cost: float
    order_date: datetime
    order_status: str

    class Config:
        from_attributes = True


class OrderInDBBase(OrderBase):
    id: int


class OrderModel(OrderInDBBase):
    pass


class OrderOut(BaseModel):
    order: OrderInDBBase
    order_items: OrderItemInDBBase | list[OrderItemInDBBase]
