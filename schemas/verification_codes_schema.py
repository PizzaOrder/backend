from pydantic import BaseModel


class VerificationCodesBase(BaseModel):
    code: int
    user_id: int
