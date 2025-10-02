from pydantic import BaseModel, Field, EmailStr

class create_user_request(BaseModel):
    name: str
    email: EmailStr

class create_post_request(BaseModel):
    user_name: str
    user_email: EmailStr
    title: str= Field(
        title="Post Title",
        min_length = 1,
        max_length = 250
      )
    content: str= Field(
        title = "Post Content",
        min_length = 1
    )
