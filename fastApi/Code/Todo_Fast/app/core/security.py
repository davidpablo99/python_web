from passlib.context import CryptContext
from typing import Union, Any
from datetime import datetime, timedelta
from jose import jwt
from core.config import settings

password_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

# Cripografia da senha
def get_password(password: str) -> str:
    if len(password.encode('utf-8')) > 72:
        raise ValueError('Senha não pode exceder 72 bytes em UTF-8')
    return password_context.hash(password)

# Verificação da senha
def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES
        )
    info_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }
    
    jwt_encoded = jwt.encode(
        info_jwt,
        settings.JWT_SECRET_KEY,
        settings.ALGORITHM
    )
    return jwt_encoded


def create_reflesh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
    info_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }
    
    jwt_encoded = jwt.encode(
        info_jwt,
        settings.JWT_REFRESH_KEY,
        settings.ALGORITHM
    )
    return jwt_encoded