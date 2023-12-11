from sqlalchemy.orm import Session

from core.models.cities import City


def get_all_cities(db: Session):
    return db.query(City).all()
