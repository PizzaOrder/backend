from pydantic import EmailStr
from sqlalchemy.orm import Session

from core.models import User
from schemas.users_schema import UserBase, UserCredentials


def old_create_user(user_data: UserBase, db: Session):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_user(user_data: UserCredentials, db: Session):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_in_db(user_mail: EmailStr, db: Session):
    return db.query(User).filter_by(email=user_mail).first()
