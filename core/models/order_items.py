from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from core.models.base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    pizza_id = Column(Integer, ForeignKey("pizzas.id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="order_items")
