from sqlalchemy.orm import Session

from auth.security.email import send_email
from auth.security.random_code_gen import generate_totp
from core.config import Settings
from core.models import VerificationCode


def store_token_in_db(secret_param: str, user_id_param: int, db: Session):
    validation_code_model = VerificationCode(secret=secret_param, user_id=user_id_param)
    db.add(validation_code_model)
    db.commit()
    db.refresh(validation_code_model)
    return validation_code_model


def send_verification_code(code_param: int, recipient_email: str) -> None:
    subject = "Код верификации PizzaOrder"
    body = f"Ваш код для входа в личный кабинет: {code_param}"
    send_email(
        sender_email_param=Settings().SENDER_EMAIL,
        sender_password_param=Settings().SENDER_PASSWORD,
        recipient_email_param=recipient_email,
        subject_param=subject,
        body_param=body,
    )


def get_code(user_id_param, db: Session):
    secret = db.query(VerificationCode).filter_by(user_id=user_id_param).first().secret
    return generate_totp(secret)
