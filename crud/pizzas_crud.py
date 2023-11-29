from sqlalchemy.orm import Session

from core.models import Pizza


def get_all_pizzas(db: Session):
    return db.query(Pizza).all()
