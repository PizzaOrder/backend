from sqlalchemy import Column, ForeignKey, Integer, String

from core.models.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    street = Column(String)
    house = Column(String)
    floor = Column(String, nullable=True)
    apartment = Column(String, nullable=True)
