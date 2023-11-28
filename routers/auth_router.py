from typing import Annotated

import pendulum
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session

from core.config import Settings
from crud.users_crud import get_user_in_db
from crud.verification_codes_crud import generate_save_and_send_code, get_code
from schemas.users_schema import UserCredentials, UserCredentialsWithCode
from utils.get_db import get_db

router = APIRouter(prefix="/auth", tags=["authentication"])


def create_access_token(data: dict, issued_at):
    data["iat"] = issued_at
    expire = issued_at.add(minutes=30).timestamp()
    data["exp"] = expire

    return jwt.encode(data, Settings().SECRET_KEY_JWT, algorithm=Settings().ALGORITHM)


@router.post("/send_verification_code/", status_code=200)
def send_code(form_data: UserCredentials, db: Session = Depends(get_db)):
    in_db = get_user_in_db(form_data.email, db)
    if in_db is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователя с таким email не существует",
            headers={"WWW-Authenticate": "Bearer"},
        )
    generate_save_and_send_code(
        user_id=in_db.id, recipient_email_param=form_data.email, db=db
    )


@router.post("/verify_code/")
def verify(form_data: UserCredentialsWithCode, db: Session = Depends(get_db)):
    user_id = get_user_in_db(UserCredentials.email, db).id
    code = get_code(user_id, db)

    if code != form_data.verification_code:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный код",
            headers={"WWW-Authenticate": "Bearer"},
        )

    data = {"sub": form_data.email}

    token = create_access_token(data=data, issued_at=pendulum.now())
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register/")
def register(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return
