import pendulum
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth.security.random_code_gen import generate_secret, generate_totp
from auth.security.token import create_access_token
from crud.users_crud import create_user, get_user_in_db
from crud.verification_codes_crud import (
    get_code,
    send_verification_code,
    store_token_in_db,
)
from schemas.auth_schema import TokenResponse
from schemas.users_schema import UserCredentials, UserCredentialsWithCode
from utils.get_db import get_db

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login/", status_code=200, response_model=None)
def handle_login_or_register(form_data: UserCredentials, db: Session = Depends(get_db)):
    user = get_user_in_db(form_data.email, db)
    if user is not None:
        user_id = user.id
        code = get_code(user_id, db)
        send_verification_code(code, form_data.email)
        return None

    secret = generate_secret(64)
    code = generate_totp(secret)
    while not (100000 <= code <= 999999):
        secret = generate_secret(64)
        code = generate_totp(secret)
    user = create_user(form_data, db)
    store_token_in_db(secret, user.id, db)

    send_verification_code(code, form_data.email)
    return None


@router.post("/verify/", status_code=200, response_model=TokenResponse)
def verify_registration(
    form_data: UserCredentialsWithCode, db: Session = Depends(get_db)
):
    user = get_user_in_db(form_data.email, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_id = user.id
    code = get_code(user_id, db)
    if form_data.verification_code != code:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный код",
            headers={"WWW-Authenticate": "Bearer"},
        )

    data = {"sub": form_data.email}

    token = create_access_token(data=data, issued_at=pendulum.now())
    return {"access_token": token, "token_type": "bearer"}
