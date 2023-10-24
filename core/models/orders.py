from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from core.models.base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    promo_id = Column(Integer, ForeignKey("promo_codes.promo_id"))
    total_cost = Column(Float)
    order_date = Column(DateTime)
    order_status = Column(String)
