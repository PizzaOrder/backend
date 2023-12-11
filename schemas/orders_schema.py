from datetime import datetime

from pydantic import BaseModel, Field

from schemas.order_items_schema import (
    OrderItemInDBBase,
)


class OrderBase(BaseModel):
    user_id: int = Field(gt=0, default=1, description="User ID must be greater than 0")
    promo_id: int | None = Field(
        gt=0, default=None, description="Promo ID must be greater than 0"
    )
    total_cost: float
    order_date: datetime
    order_status: str

    class Config:
        from_attributes = True


class OrderInDBBase(OrderBase):
    id: int = Field(default=1)


class OrderModel(OrderInDBBase):
    pass


class OrderOut(BaseModel):
    order: OrderInDBBase
    order_items: OrderItemInDBBase | list[OrderItemInDBBase]
