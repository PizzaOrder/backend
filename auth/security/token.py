import pendulum
from jose import jwt

from core.config import Settings


def create_access_token(data: dict, issued_at: pendulum.DateTime):
    data["iat"] = issued_at
    expire = issued_at.add(minutes=30).timestamp()
    data["exp"] = expire

    return jwt.encode(data, Settings().SECRET_KEY_JWT, algorithm=Settings().ALGORITHM)


def decode_access_token(token: str):
    ...
