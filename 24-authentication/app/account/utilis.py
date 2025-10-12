from datetime import timedelta, datetime, timezone
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.account.models import RefreshToken, User
import uuid
from app.account.models import RefreshToken
from app.db.config import SessionLocal
from sqlalchemy import select

SECRET_KEY = "ahhdadajdjdadadjadjajdgadaasfrfjd"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(userid, token_given, expiresat):
    with SessionLocal() as session:
        refresh_token = RefreshToken(
            user_id=userid,
            token=token_given,
            expires_at=expiresat,
            created_at=datetime.now(timezone.utc),
            revoked=False,
        )
        session.add(refresh_token)
        session.commit()
        session.refresh(refresh_token)
        return True


def create_tokens(user: User, refresh_token_given: str = None):
    access_token = create_access_token(data={"sub": str(user.id)})
    if not refresh_token_given:
        refresh_token = str(uuid.uuid4())
        expires_at = datetime.now(timezone.utc) + timedelta(days=7)
        create_refresh_token(user.id, refresh_token, expires_at)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
    else:
        return {
            "access_token": access_token,
            "refresh_token": refresh_token_given,
            "token_type": "bearer",
        }


def verify_refresh_token(token: str):
    with SessionLocal() as session:
        statement = select(RefreshToken).where(RefreshToken.token == token)
        db_token = session.scalar(statement)
        if db_token and not db_token.revoked:
            expires_at = db_token.expires_at
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=timezone.utc)
            if expires_at > datetime.now(timezone.utc):
                statement = select(User).where(User.id == db_token.user_id)
                return session.scalar(statement)
        return None
