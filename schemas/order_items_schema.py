from pydantic import BaseModel


class OrderItemBase(BaseModel):
    pizza_id: int
    quantity: int

    class Config:
        from_attributes = True


class OrderItemWithOrderId(OrderItemBase):
    order_id: int


class OrderItemInDBBase(OrderItemWithOrderId):
    id: int


class OrderItemModel(OrderItemInDBBase):
    pass
