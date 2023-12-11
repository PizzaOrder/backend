from sqlalchemy.orm import Session

from core.models.promo_codes import PromoCode


def promo_code_exists(promo_code: str, db: Session):
    return db.query(PromoCode).filter_by(code=promo_code).first()


def get_all_promo_codes(db: Session):
    return db.query(PromoCode).all()


def get_latest_special_offers(db: Session, limit: int = 3):
    return db.query(PromoCode).order_by(PromoCode.start_date).limit(limit).all()
