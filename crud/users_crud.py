from sqlalchemy.orm import Session

from core.models import User
from schemas.users_schema import UserBase


def create_user(user_data: UserBase, db: Session):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
