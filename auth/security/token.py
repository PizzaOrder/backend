import pendulum
from jose import JWTError, jwt

from core.config import Settings


def create_access_token(data: dict, issued_at: pendulum.DateTime):
    data["iat"] = issued_at
    expire = issued_at.add(hours=24).timestamp()
    data["exp"] = expire

    return jwt.encode(data, Settings().SECRET_KEY_JWT, algorithm=Settings().ALGORITHM)


def decode_access_token(access_token: str, token_type: str, credentials_exceptions):
    try:
        return jwt.decode(
            token=access_token,
            key=Settings().SECRET_KEY_JWT,
            algorithms=Settings().ALGORITHM,
        )
    except JWTError as e:
        raise credentials_exceptions from e
