from typing import Annotated

import pendulum
from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from core.models import Order
from crud.order_items_crud import create_order_items
from crud.pizzas_crud import get_pizza, get_pizza_prices
from crud.promo_code_crud import promo_code_exists
from middlewares.get_user_middleware import get_user_by_token
from schemas.order_items_schema import OrderItemBase
from schemas.orders_schema import OrderBase
from utils.get_db import get_db

router = APIRouter(prefix="/order", tags=["order"])


@router.post("/new/")
def create_new_order(
    order_items: OrderItemBase | list[OrderItemBase],
    current_user=Depends(get_user_by_token),
    promo_code=Annotated[str, Body()],
    db: Session = Depends(get_db),
):
    create_order_items(order_items, db)

    user_id = current_user.id
    promo_id = (
        promo_code_exists(promo_code, db).id
        if promo_code_exists(promo_code, db) is not None
        else None
    )

    if isinstance(order_items, list):
        total_cost = get_pizza_prices([item.pizza_id for item in order_items], db)
    else:
        total_cost = get_pizza(order_items.pizza_id, db)
    order_time = pendulum.now()
    status = "Создан"
    order_base = OrderBase(
        user_id=user_id,
        promo_id=promo_id,
        total_cost=total_cost,
        order_date=order_time,
        order_status=status,
    )

    order = Order(**order_base.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
