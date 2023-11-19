from sqlalchemy.orm import Session
from core.models.promo_codes import PromoCode


def promo_code_exists(promo_code: str, db: Session):
    return db.query(PromoCode).filter_by(code=promo_code).first()
