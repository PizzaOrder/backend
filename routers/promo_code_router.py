from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from crud.promo_code_crud import promo_code_exists, get_all_promo_codes
from utils.get_db import get_db

router = APIRouter(prefix="/promo_codes", tags=["promo code"])


@router.get("validate/{promo_code}")
def validate_promo_code(
    promo_code: Annotated[str, Path()], db: Session = Depends(get_db)
):
    return promo_code_exists(promo_code, db)


@router.get("")
def get_promo_codes(db: Session = Depends(get_db)):
    return get_all_promo_codes(db)
