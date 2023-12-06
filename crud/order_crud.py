from sqlalchemy.orm import Session, selectinload

from core.models import Order


def create_order(schema, user_id: int, db: Session):
    return ...


def get_all_orders_for_admin(db: Session):
    return db.query(Order).options(selectinload(Order.order_items)).all()
