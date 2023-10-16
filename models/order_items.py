from sqlalchemy import Column, ForeignKey, Integer
from utils.database_orm import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    pizza_id = Column(Integer, ForeignKey("default_pizzas.pizza_id"))
    quantity = Column(Integer)
