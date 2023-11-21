from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.users_crud import create_user
from schemas.users_schema import UserBase
from utils.get_db import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create/")
def register_user(user_data: UserBase, db: Session = Depends(get_db)):
    return create_user(user_data, db)
