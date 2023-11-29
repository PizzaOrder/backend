from sqlalchemy import Column, DateTime, Integer, String

from core.models.base import Base


class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    discount_percentage = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
