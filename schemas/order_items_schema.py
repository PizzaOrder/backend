from pydantic import BaseModel, Field, field_validator


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


class OrderUpdate(BaseModel):
    order_id: int = Field(default=1, gt=0)
    new_status: str = Field(default="Готовится")

    @field_validator("new_status")
    def validate_new_status(cls, value):
        allowed_statuses = ["Принят", "Готовится", "Готов", "Выдан"]
        if value not in allowed_statuses:
            raise ValueError(
                f"Invalid new_status value."
                f" Allowed values: {', '.join(allowed_statuses)}"
            )
        return value
