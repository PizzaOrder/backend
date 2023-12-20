from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm import Session

from auth.security.token import decode_access_token
from core.models import User
from schemas.users_schema import UserBase, UserCredentials, UserInDBBase


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


def get_user_by_token(access_token: str, db: Session) -> UserInDBBase:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(access_token, "5", credentials_exception)

    user = get_user_in_db(payload["sub"], db)
    if user is None:
        raise credentials_exception
    return user
