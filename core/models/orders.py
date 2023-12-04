from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.models.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    promo_id = Column(Integer, ForeignKey("promo_codes.id"))
    total_cost = Column(Float)
    order_date = Column(DateTime)
    order_status = Column(String)

    order_items = relationship('OrderItem', 'order')
