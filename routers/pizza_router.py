from fastapi import APIRouter, Depends
from models.pizzas import Pizza
from schemas.pizzas_schema import PizzaBase
from sqlalchemy.orm import Session
from utils.get_db import get_db

router = APIRouter(prefix="/pizzas", tags=["pizza"])


@router.get("")
async def get_pizzas(db: Session = Depends(get_db)) -> list[PizzaBase]:
    return db.query(Pizza).all()
