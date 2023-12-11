from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from crud.order_crud import change_order_status, get_all_orders_for_admin
from crud.user_role_crud import is_user_admin
from crud.users_crud import get_user_by_token
from schemas.order_items_schema import OrderUpdate
from utils.get_db import get_db

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/order/")
def get_all_orders(token: Annotated[str, Header()], db: Session = Depends(get_db)):
    current_user = get_user_by_token(token, db)
    if is_user_admin(current_user.id, db):
        return get_all_orders_for_admin(db)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden"
        )


@router.put("/order/{order_id}/")
def update_order(
    order_update: OrderUpdate,
    token: Annotated[str, Header()],
    db: Session = Depends(get_db),
):
    current_user = get_user_by_token(token, db)
    if not is_user_admin(current_user.id, db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden"
        )
    if order_update.new_status in ["Принят", "Готовится", "Готов", "Выдан"]:
        return change_order_status(order_update, db)

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid new_status value"
        )
