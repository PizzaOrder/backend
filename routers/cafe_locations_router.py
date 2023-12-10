from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.cafe_locations_crud import get_cafe_locations, get_cafes_in_city
from utils.get_db import get_db

router = APIRouter(prefix="/cafes", tags=["cafe"])


@router.get("/")
def get_cities(db: Session = Depends(get_db)):
    return get_cafe_locations(db)


@router.get("/city/{city_name}")
def get_cities_by_name(city_name: str, db: Session = Depends(get_db)):
    return get_cafes_in_city(city_name, db)
