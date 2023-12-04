from typing import Annotated

from fastapi import Header, HTTPException, status
from sqlalchemy.orm import Session

from auth.security.token import decode_access_token
from crud.users_crud import get_user_in_db


def get_user_by_token(access_token: Annotated[str, Header()], db: Session):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(access_token[1:-1], "5", credentials_exception)

    user = get_user_in_db(payload["sub"], db)
    if user is None:
        raise credentials_exception
    return user
