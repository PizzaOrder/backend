from sqlalchemy.orm import Session, selectinload

from core.models.cafe_locations import CafeLocation


def get_cafe_locations(db: Session):
    return db.query(CafeLocation).options(selectinload(CafeLocation.city)).all()
