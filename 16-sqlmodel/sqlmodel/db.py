from sqlmodel import create_engine, SQLModel, MetaData
metadata = MetaData()

DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(DATABASE_URL, echo = True)

def create_tables():
    SQLModel.metadata.create_all(engine)