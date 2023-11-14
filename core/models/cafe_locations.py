from core.models.base import Base
from sqlalchemy import Integer, String, ForeignKey, Column


class CafeLocation(Base):
    __tablename__ = "cafe_locations"

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    street = Column(String)
    house = Column(String)
