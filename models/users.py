from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from utils.database_orm import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    telephone = Column(Integer)

    @hybrid_property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"