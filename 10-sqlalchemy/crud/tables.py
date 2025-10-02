from db import engine
from sqlalchemy import ForeignKey, Table, MetaData, Integer, String, Column

metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key = True, nullable=False),
    Column("name", String, nullable = False),
    Column("email", String, nullable = False)
   )

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key= True),
    Column("user_name",String , ForeignKey("users.id"), nullable = False
           ),
    Column("title", String, nullable = False),
    Column("content", String, nullable = False)
)

def create_tables():
    metadata.create_all(engine)

create_tables()

