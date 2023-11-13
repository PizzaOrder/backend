from core.models.cities import City
from sqlalchemy.orm import Session


def get_all_cities(db: Session):
    return db.query(City).all()
