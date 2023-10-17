from models.pizzas import Pizza
from sqlalchemy.orm import Session


def get_all_pizzas(db: Session):
    return db.query(Pizza).all()
