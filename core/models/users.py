from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from core.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    email = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user_role = relationship("UserRole", back_populates="user")
    verification_code = relationship("VerificationCode", back_populates="user")

    @hybrid_property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
