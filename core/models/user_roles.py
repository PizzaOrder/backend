from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.models.base import Base


class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    role = Column(String)

    user = relationship("User", back_populates="user_role")

    __table_args__ = (CheckConstraint(role.in_(["user", "admin"]), name="check_role"),)
