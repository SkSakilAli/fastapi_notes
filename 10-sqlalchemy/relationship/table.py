from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

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

#One To Many Relation
posts = Table(
   "posts",
   metadata,
   Column("id", Integer, primary_key=True),
   Column("user_id", Integer, ForeignKey("users.id",
   ondelete ="CASCADE"), nullable= False ), #Add unique = True for one to one relationship
   Column("title", String, nullable = False),
   Column("content", String, nullable = False)
)

#Creating Table
def create_tables():
   metadata.create_all(engine) #engine is the giving loaction of db where the data is to be crated

#deleting tables
def drop_tables():
   metadata.drop_all(engine)

