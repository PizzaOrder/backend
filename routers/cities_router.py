from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.cities_crud import get_all_cities
from utils.get_db import get_db

router = APIRouter(prefix="/cities", tags=["city"])


@router.get("")
async def get_cities(db: Session = Depends(get_db)):
    return get_all_cities(db)
