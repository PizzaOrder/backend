from sqlalchemy import Integer, Column, String, Float
from utils.database_orm import Base


class DefaultPizza(Base):
    __tablename__ = 'default_pizzas'

    pizza_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
