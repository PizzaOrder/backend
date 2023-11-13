from sqlalchemy import Column, Integer, String
from core.models.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    street = Column(String)
    house = Column(String)
    floor = Column(String, nullable=True)
    apartment = Column(String, nullable=True)
