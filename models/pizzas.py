from sqlalchemy import Column, Float, Integer, String
from utils.database_orm import Base


class Pizza(Base):
    __tablename__ = "pizzas"

    pizza_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
