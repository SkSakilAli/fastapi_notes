##We first have to create an engine to use sqlalchemy globally i.e one time
import db
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./sqlite.db"
engine = create_engine(DATABASE_URL, echo=True) # echo=True is only for testing don't use it in development

