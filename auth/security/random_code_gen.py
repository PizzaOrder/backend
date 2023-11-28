import pyotp


def generate_secret(num_bytes: int = 64) -> str:
    return pyotp.random_base32(num_bytes)


def generate_totp(secret: str) -> int:
    totp = pyotp.TOTP(
        secret,
        digits=6,
        interval=1800,
    )
    return int(totp.now())
