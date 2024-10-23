import jwt

from core.settings import settings


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.jwt_token.public_key.read_text(),
    algorithm: str = settings.jwt_token.algorithm,
    audience: str = settings.jwt_token.audience,
) -> dict:
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
        audience=audience,
    )
    return decoded
