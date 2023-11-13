from core.models.base import Base
from sqlalchemy import Integer, Column, ForeignKey


class UserAddresses(Base):
    __tablename__ = "user_addresses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    address_id = Column(Integer, ForeignKey("addresses.id"))
