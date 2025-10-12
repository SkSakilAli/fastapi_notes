from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    is_active: bool = True
    is_admin: bool = False
    password: str
