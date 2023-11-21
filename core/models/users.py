from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.hybrid import hybrid_property
from core.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    telephone = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    @hybrid_property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
