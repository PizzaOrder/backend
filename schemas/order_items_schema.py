from pydantic import BaseModel


class OrderItemBase(BaseModel):
    order_id: int
    pizza_id: int
    quantity: int

    class Config:
        from_attributes = True


class OrderItemInDBBase(OrderItemBase):
    id: int


class OrderItem(OrderItemInDBBase):
    pass
