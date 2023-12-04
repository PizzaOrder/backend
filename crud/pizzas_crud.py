from sqlalchemy.orm import Session

from core.models import Pizza


def get_all_pizzas(db: Session):
    return db.query(Pizza).all()


def get_pizza_prices(pizzas_id: list, db: Session) -> float:
    models = db.query(Pizza).filter(Pizza.id.in_(pizzas_id)).all()
    return sum(pizza.price for pizza in models)


def get_pizza(pizza_id: int, db: Session) -> float:
    return db.query(Pizza).filter_by(id=pizza_id).first().price
