import pendulum
from sqlalchemy import Column, DateTime, String, ForeignKey, Integer

from sqlalchemy.orm import relationship

from core.models.base import Base


class VerificationCode(Base):
    __tablename__ = "verification_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=pendulum.now("UTC"))
    expiration_at = Column(DateTime, default=pendulum.now().add(minutes=30))

    user = relationship("User", back_populates="verification_code")
