from models import User, Post
from db import SessionLocal
from sqlalchemy import select, asc
#Create a User
def create_user(name: str, email:str):
    with SessionLocal() as session:
          user = User(name= name, email= email)
          session.add(user)
          session.commit()
          session.refresh(user)
          return user
    
#Read User By Id
def get_user_by_id(user_id: int):
     with SessionLocal() as session:
          user = session.get_one(User, user_id) #get_one return only one object if present otherwise exception
          return user
     
#Read Post by ID
def get_post_by_id(post_id: int):
     with SessionLocal() as session:
          statement = select(Post).where(Post.id == post_id)
          session.scalars(statement).one() #to get all posts do .all()

# Read all posts by an User
def get_post_by_user(user_id : int):
     with SessionLocal() as session:
          user = session.get(User, user_id)
          posts = user.posts if user else []
          return posts
     
#Update User Email
def update_user_email(user_id: int, new_email):
     with SessionLocal() as session:
          user = session.get(User, user_id)
          user.email = new_email
          return user
     
#Delete Post
def delete_post(post_id : int):
     with SessionLocal() as session:
          post = session.get(Post, post_id)
          if post:
            session.delete()
            session.commit()
          else:
               return "Post Does Not Exist"
#Order By
def get_users_by_name():
     with SessionLocal() as session:
          statement = select(User).order_by(asc(User.name))
          users =session.scalars(statement)
          return users