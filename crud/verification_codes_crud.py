from sqlalchemy.orm import Session

from auth.security.email import send_email
from auth.security.random_code_gen import generate_totp
from core.config import Settings
from core.models import VerificationCode


def create_verification_codes_in_db(code_param: int, user_id_param: int, db: Session):
    validation_code_model = VerificationCode(code=code_param, user_id=user_id_param)
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


def generate_save_and_send_code(user_id, recipient_email_param, db: Session):
    totp_code = generate_totp(Settings().TOTP_SECRET)
    create_verification_codes_in_db(totp_code, user_id, db)
    send_verification_code(totp_code, recipient_email_param)
    return totp_code


def get_code(user_id_param, db: Session):
    return db.query(VerificationCode).filter_by(user_id=user_id_param).first()
