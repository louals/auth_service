from pydantic import BaseModel, EmailStr
from typing import Literal

class User(BaseModel):
    email: EmailStr
    username: str
    password: str
    role: Literal["admin", "user"] = "user"  

class UserLogin(BaseModel):
    email: EmailStr
    password: str
