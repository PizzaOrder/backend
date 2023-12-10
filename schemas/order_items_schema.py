from pydantic import BaseModel, Field


class OrderItemBase(BaseModel):
    pizza_id: int = Field(
        gt=0, default=1, description="Pizza ID must be greater than 0"
    )
    quantity: int = Field(
        gt=0, default=1, description="Quantity must be greater than 0"
    )

    class Config:
        from_attributes = True


class OrderItemWithOrderId(OrderItemBase):
    order_id: int


class OrderItemInDBBase(OrderItemWithOrderId):
    id: int


class OrderItemModel(OrderItemInDBBase):
    pass
