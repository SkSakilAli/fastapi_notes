from sqlmodel import Session
from db import engine
from models import User


def create_user(name: str, email: str):
    with Session(engine) as session: #we use with ... as .. because it does automatically destroies/closes itself like did in case of file opening
          user = User(name =name, email = email)
          session.add(user)
          session.commit()
          session.refresh(user)
          return user

