from db import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete, asc, text #TEXT ALLOWS TO WRITE SQL ALCHEMY DIRECTLY

#Insert or create user
def create_a_user(name: str, email: str):
    with engine.connect() as conn: #creates a database connection and executes operations
            statement = insert(users).values(name=name, email= email)
            #variable = insert(table_anme).values(column_name= value)
            conn.execute(statement) #executes the statement
            conn.commit() #commit the changes

def create_a_post(user_id: str, title: str, content: str):
      with engine.connect() as conn:
            statement = insert(posts).values(user_name = user_id, title=title, content= content)
            conn.execute(statement)
            conn.commit()
def get_posts_by_user(user_name: str):
      with engine.connect() as conn:
            statement = select(posts).where(posts.c.user_name == user_name)
            result = conn.execute(statement).fetchall
            return result
      
#update user email
def update_user_email(user_name: str, new_email: str):
      with engine.connect() as conn:
            statement = update(users).where(users.c.user_name==user_name).values(email = new_email)
            conn.execute(statement)
            conn.commit()

      #delete post
def delete_post(post_id: int):
            with engine.connect as conn:
                  statement = delete(posts).where(posts.c.id == post_id)
                  conn.execute(statement)
                  conn.commit()

      #Get all Users Ordered by Name (A-Z)
def get_users_ordered_by_name():
            with engine.connect as conn:
                  statement = select(users).order_by(asc(users.c.name))
                  result = conn.execute(statement).fetchall()

# Join users and posts (List all posts with author name)
def get_posts_with_author():
       with engine.connect as conn:
              statement = select(
                     posts.c.id,
                     posts.c.title,
                     users.c.name.lable("author name")
              ).join(users, posts.c.user_id == users.c.id)
              result = conn.execute(statement).fetchall
              return result
       
#Writing RAW SQL

#(INSERT)
def raw_sql_insert():
       with engine.connect() as conn:
              statement = text("""
             INSERT INTO users (name, email)
             VALUES (:name, :email)                  
""")
              conn.execute(statement, {"name": "Sakil", "email":"sakil@mail.com"})
              conn.commit()


# SELECT
def raw_sql_example():
       with engine.connect() as conn:
              statement = text("SELECT * FROM users WHERE email = :email")
              result = conn.execute(statement, {"email":"sakil@mail.com"}).first