from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.order_items_crud import create_order_items
from schemas.order_items_schema import OrderItemBase
from schemas.orders_schema import OrderBase
from utils.get_db import get_db

router = APIRouter(prefix="/order", tags=["order"])


@router.post("/new/")
def create_new_order(
        order: OrderBase,
        order_items_param: OrderItemBase | list[OrderItemBase],
        db: Session = Depends(get_db)
):
    return create_order_items(order_items_param, db)
