from datetime import datetime

from pydantic import BaseModel


class PromoCodeBase(BaseModel):
    code: str
    discount_percentage: int

    class Config:
        from_attributes = True


class PromoCodeWithTime(PromoCodeBase):
    start_date: datetime
    end_date: datetime


class PromoCodeInDBBase(PromoCodeWithTime):
    img_source: str
    id: int


class PromoCodeModel(PromoCodeInDBBase):
    pass
