from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from core.config import Settings
from crud.users_crud import get_user_in_db
from schemas.users_schema import UserBase
from utils.get_db import get_db

router = APIRouter(prefix="/user", tags=["users"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/me/", response_model=UserBase)
def get_current_user(access_token: Annotated[str, Header()],
                     token_type: Annotated[str, Header()],
                     db: Session = Depends(get_db)
                     ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            access_token, Settings().SECRET_KEY_JWT, algorithms=Settings().ALGORITHM
        )
    except JWTError as e:
        raise credentials_exception from e

    user = get_user_in_db(payload['sub'], db)
    if user is None:
        raise credentials_exception

    return user
