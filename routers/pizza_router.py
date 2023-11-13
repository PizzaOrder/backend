from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.pizzas_crud import get_all_pizzas
from schemas.pizzas_schema import PizzaModel
from utils.get_db import get_db

router = APIRouter(prefix="/pizzas", tags=["pizza"])


@router.get("", response_model=list[PizzaModel])
async def get_pizzas(db: Session = Depends(get_db)):
    return get_all_pizzas(db)
