from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    name: str = Field(..., title="Name of the user")
    email: EmailStr = Field(..., title="Email of the user")
    password: str = Field(..., title="Password of the user")
    school: Optional[str] = Field(None, title="School of the user")
    bio: Optional[str] = Field(None, title="Bio of the user")
    standard: Optional[int] = Field(None, title="Standard of the user")
    
class LoginUser(BaseModel):
    email: EmailStr
    password: str