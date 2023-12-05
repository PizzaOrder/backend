from typing import Annotated

import pendulum
from fastapi import APIRouter, Body, Depends, Header
from sqlalchemy.orm import Session, selectinload

from core.models import Order
from crud.order_items_crud import create_order_items
from crud.pizzas_crud import get_pizza, get_pizza_prices
from crud.promo_code_crud import promo_code_exists
from crud.users_crud import get_user_by_token
from schemas.order_items_schema import OrderItemBase, OrderItemWithOrderId
from schemas.orders_schema import OrderBase, OrderInDBBase, OrderOut
from utils.get_db import get_db

router = APIRouter(prefix="/order", tags=["order"])


@router.post("/new/")
def create_new_order(
    order_items: OrderItemBase | list[OrderItemBase],
    token: Annotated[str, Header()],
    promo_code: Annotated[str, Body()] = None,
    db: Session = Depends(get_db),
):
    current_user = get_user_by_token(token, db)

    user_id = current_user.id
    promo_id = (
        promo_code_exists(promo_code, db).id
        if promo_code_exists(promo_code, db) is not None
        else None
    )

    if isinstance(order_items, list):
        total_cost = get_pizza_prices([item.pizza_id for item in order_items], db)
    else:
        total_cost = get_pizza(order_items.pizza_id, db).price
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

    order = OrderInDBBase(**order.__dict__)

    if isinstance(order_items, list):
        order_items = [
            OrderItemWithOrderId(**x.model_dump(), order_id=order.id)
            for x in order_items
        ]
    else:
        order_items = OrderItemWithOrderId(
            **order_items.model_dump(), order_id=order.id
        )

    order_items = create_order_items(order_items, db)
    return OrderOut(order=order, order_items=order_items)


@router.get("/user/")
def get_user_orders(token: Annotated[str, Header()], db: Session = Depends(get_db)):
    current_user = get_user_by_token(token, db)
    return (
        db.query(Order)
        .options(selectinload(Order.order_items))
        .filter_by(user_id=current_user.id)
        .all()
    )
