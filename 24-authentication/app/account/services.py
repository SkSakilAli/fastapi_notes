from app.account.models import User, RefreshToken
from app.account.schema import UserCreate
from app.db.config import SessionLocal
from app.account.utilis import hash_password, verify_password
from sqlalchemy import select
from fastapi import FastAPI, HTTPException


def create_user(user: UserCreate):
    with SessionLocal() as session:
        statement = select(User).where(User.email == user.email)
        if session.scalars(statement).all():
            raise HTTPException(status_code=400, detail="Email Already Exist")
        else:
            new_user = User(
                email=user.email,
                name=user.name,
                hashed_password=hash_password(user.password),
                is_verified=False,
                is_active=user.is_active,
                is_admin=user.is_admin,
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user


def get_user(user_email: str):
    try:
        with SessionLocal() as session:
            statement = select(User).where(User.email == user_email).one()
    except:
        pass


def authenticate_user(email: str, password: str):
    with SessionLocal() as session:
        statement = select(User).where(User.email == email)
        try:
            user = session.scalars(statement).one()
            hashed_password = user.hashed_password
            if verify_password(password, hashed_password):
                return user
            else:
                return False

        except:
            raise HTTPException(status_code=404, detail="Email Does Not Exist!")


def create_refresh_token(userid, token_given, expiresat):
    with SessionLocal() as session:
        refresh_token = RefreshToken(
            user_id=userid, token=token_given, expires_at=expiresat
        )
        session.add(refresh_token)
        session.commit()
        session.refresh(refresh_token)
        return True
