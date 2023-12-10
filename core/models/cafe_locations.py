from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.models.base import Base


class CafeLocation(Base):
    __tablename__ = "cafe_locations"

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    street = Column(String)
    house = Column(String)

    city = relationship("City", back_populates="cafes", single_parent=True)
