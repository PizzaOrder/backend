from sqlalchemy.orm import Session

from core.models import User
from schemas.users_schema import UserBase, UserCredentials


def create_user(user_data: UserBase, db: Session):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def check_user_in_db(user_data: UserCredentials, db: Session):
    return db.query(User).filter_by(email=user_data.email).first()
