from sqlalchemy.orm import Session, selectinload

from core.models import User


def is_user_admin(user_id: int, db: Session) -> bool:
    user = (db.query(User).filter_by(id=user_id).
            options(selectinload(User.user_role)).one())
    user_role = user.user_role[0].role == 'admin'

    return user_role
