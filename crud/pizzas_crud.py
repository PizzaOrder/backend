from models.pizzas import Pizza
from schemas.pizzas_schema import PizzaBase
from sqlalchemy.orm import Session


def get_all_pizzas(db: Session) -> list[PizzaBase]:
    return db.query(Pizza).all()
