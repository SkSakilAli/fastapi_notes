from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, MetaData, ForeignKey
from db import engine

metadata = MetaData()
class Base(DeclarativeBase):
    pass

#User Model/Table

class User(Base):
    __tablename__ = "user" #Table Name
   
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    name: Mapped[str] = mapped_column(String(50), nullable = False)
    email: Mapped[str] = mapped_column(String(50), nullable = False, unique=True)

   #One to Many Users post
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete") 

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id", ondelete = "CASCADE"))
    title: Mapped[str] = mapped_column(String, nullable = False)
    content: Mapped[str] = mapped_column(String, nullable = False)
     
    user: Mapped["User"] = relationship("User", back_populates="posts")

   #create table
def create_table():
   Base.metadata.create_all(engine)
# For many to many we need model and association table

if __name__ == "__main__":
 create_table()