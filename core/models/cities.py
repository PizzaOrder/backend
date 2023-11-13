from sqlalchemy import Column, Integer, String

from core.models.base import Base


class Cities(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    city = Column(String)
