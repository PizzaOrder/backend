from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.cafe_locations_crud import get_cafe_locations
from utils.get_db import get_db

router = APIRouter(prefix="/cafes", tags=["cafe"])


@router.get("/")
def get_cities(db: Session = Depends(get_db)):
    return get_cafe_locations(db)
