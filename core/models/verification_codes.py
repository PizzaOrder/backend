from sqlalchemy import Column, String, ForeignKey, Integer

from sqlalchemy.orm import relationship

from core.models.base import Base


class VerificationCode(Base):
    __tablename__ = "verification_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="verification_code")
