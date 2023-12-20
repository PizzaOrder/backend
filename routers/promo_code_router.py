from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from crud.promo_code_crud import (
    get_all_promo_codes,
    get_latest_special_offers,
    promo_code_exists,
)
from schemas.promo_codes_schema import PromoCodeBase, PromoCodeModel
from utils.get_db import get_db

router = APIRouter(prefix="/promo_codes", tags=["promo code"])


@router.get("/validate/{promo_code}", response_model=PromoCodeBase | None)
def validate_promo_code(
    promo_code: Annotated[str, Path()], db: Session = Depends(get_db)
):
    promo_code = promo_code.upper()
    exists = promo_code_exists(promo_code, db)
    if exists:
        return exists
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Promo code not found"
        )


@router.get("", response_model=list[PromoCodeModel] | PromoCodeModel)
def get_promo_codes(db: Session = Depends(get_db)):
    return get_all_promo_codes(db)


@router.get("/latest", response_model=list[PromoCodeModel] | PromoCodeModel)
def get_latest_promo_codes(db: Session = Depends(get_db)):
    return get_latest_special_offers(db, 3)
