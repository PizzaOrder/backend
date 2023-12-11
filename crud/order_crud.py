from sqlalchemy.orm import Session, selectinload

from core.models import Order
from schemas.order_items_schema import OrderUpdate


def create_order(schema, user_id: int, db: Session):
    return ...


def get_all_orders_for_admin(db: Session):
    return db.query(Order).options(selectinload(Order.order_items)).all()


def get_order_by_id(order_id: int, db: Session):
    return db.query(Order).filter_by(id=order_id).first()


def change_order_status(order_update: OrderUpdate, db: Session):
    order = get_order_by_id(order_update.order_id, db)
    order.order_status = order_update.new_status
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
