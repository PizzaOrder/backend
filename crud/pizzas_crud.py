from typing import Type

from models.pizzas import Pizza
from sqlalchemy.orm import Session


def get_all_pizzas(db: Session) -> list[Type[Pizza]]:
    return db.query(Pizza).all()
