from sqlalchemy.orm import Session

from core.models import OrderItem
from schemas.order_items_schema import OrderItemBase


def create_order_items(order_items_param: OrderItemBase | list[OrderItemBase], db: Session):
    if isinstance(order_items_param, list):
        order_items = [OrderItem(**item.model_dump()) for item in order_items_param]
        db.add_all(order_items)
    else:
        order_items = OrderItem(**order_items_param.model_dump())
        db.add(order_items)

    db.commit()
    db.refresh(order_items)
    return order_items
