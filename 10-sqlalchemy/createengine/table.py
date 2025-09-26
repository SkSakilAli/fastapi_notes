from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

#User Table
#Creating table structure
users = Table(
    "users", #Table Name
    metadata, #Required
    Column("id", Integer, primary_key= True), #Creating Column in DB
    Column("name", String(length=50), nullable = False ),
    Column("email", String, nullable = False, unique= True)
)

#Creating Table
def create_tables():
   metadata.create_all(engine) #engine is the giving loaction of db where the data is to be crated

#deleting tables
def drop_tables():
   metadata.drop_all(engine)

create_tables()