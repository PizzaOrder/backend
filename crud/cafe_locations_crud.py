from sqlalchemy.orm import Session, selectinload

from core.models import City
from core.models.cafe_locations import CafeLocation


def get_cafe_locations(db: Session):
    return db.query(CafeLocation).options(selectinload(CafeLocation.city)).all()


def get_cafes_in_city(city_param: str, db: Session):
    if city := db.query(City).filter_by(city=city_param).first():
        return (
            db.query(CafeLocation)
            .filter_by(city_id=city.id)
            # .options(selectinload(CafeLocation.city))
            .all()
        )
    else:
        return None
