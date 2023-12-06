from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from crud.order_crud import get_all_orders_for_admin
from crud.user_role_crud import is_user_admin
from crud.users_crud import get_user_by_token
from schemas.orders_schema import OrderOut
from utils.get_db import get_db

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/order/")
def get_all_orders(
    token: Annotated[str, Header()], db: Session = Depends(get_db)
) -> list[OrderOut] | OrderOut:
    current_user = get_user_by_token(token, db)
    if is_user_admin(current_user.id, db):
        return get_all_orders_for_admin(db)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden"
        )
