from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.cities_crud import get_all_cities
from schemas.cities_schema import CityModel
from utils.get_db import get_db

router = APIRouter(prefix="/cities", tags=["city"])


@router.get("", response_model=list[CityModel] | CityModel)
async def get_cities(db: Session = Depends(get_db)):
    return get_all_cities(db)
