from sqlalchemy.orm import Session, selectinload

from core.models import User


def is_user_admin(user_id: int, db: Session) -> bool:
    return db.query(User).options(selectinload(User.user_role)).first() == "Admin"
