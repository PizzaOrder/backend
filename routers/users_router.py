from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from auth.security.token import decode_access_token
from crud.users_crud import get_user_in_db
from utils.get_db import get_db

router = APIRouter(prefix="/user", tags=["users"])


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/me/")
def get_current_user(
    access_token: Annotated[str, Header()] = None, db: Session = Depends(get_db)
):
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
