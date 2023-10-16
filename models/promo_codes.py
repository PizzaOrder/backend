from sqlalchemy import Integer, String, Column, DateTime
from utils.database_orm import Base


class PromoCode(Base):
    __tablename__ = 'promo_codes'

    promo_id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    discount_percentage = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
