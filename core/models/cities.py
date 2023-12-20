from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.models.base import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    city = Column(String)

    cafes = relationship("CafeLocation", back_populates="city")
