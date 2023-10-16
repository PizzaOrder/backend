from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, Mapped
from utils.database_orm import Base


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    city = Column(String)
    street = Column(String)
    house = Column(String)
    apartment = Column(String, nullable=True)
