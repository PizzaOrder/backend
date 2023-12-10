from datetime import datetime

from pydantic import BaseModel


class PromoCodeBase(BaseModel):
    code: str
    discount_percentage: int
    start_date: datetime
    end_date: datetime
    img_source: str

    class Config:
        from_attributes = True


class PromoCodeInDBBase(PromoCodeBase):
    id: int


class PromoCodeModel(PromoCodeInDBBase):
    pass
