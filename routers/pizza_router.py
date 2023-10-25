from fastapi import APIRouter, Depends
from core.models import Pizza
from sqlalchemy.orm import Session
from utils.get_db import get_db

router = APIRouter(prefix="/pizzas", tags=["pizza"])


@router.get("")
async def get_pizzas(db: Session = Depends(get_db)) -> list[Pizza]:
    return db.query(Pizza).all()
