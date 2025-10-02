from sqlmodel import Field, SQLModel

class User(SQLModel, table = True): #table = True will create table so it's kind of mandatory
    id: int = Field(primary_key=True)
    name: str
    email: str
