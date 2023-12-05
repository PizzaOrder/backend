from typing import Annotated

from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from crud.users_crud import get_user_by_token
from schemas.users_schema import ChangeUserProfile
from utils.get_db import get_db

router = APIRouter(prefix="/user", tags=["users"])


@router.get("/me/")
def get_current_user(
    access_token: Annotated[str, Header()] = None, db: Session = Depends(get_db)
):
    return get_user_by_token(access_token, db)


@router.put("/me/")
def update_user_profile(
    token: Annotated[str, Header()],
    user_profile: ChangeUserProfile,
    db: Session = Depends(get_db),
):
    current_user = get_user_by_token(token, db)

    if user_profile.first_name is not None:
        current_user.name = user_profile.first_name
    if user_profile.last_name is not None:
        current_user.surname = user_profile.last_name

    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
