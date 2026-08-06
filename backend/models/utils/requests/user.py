from datetime import date
from typing import Optional

from pydantic import BaseModel

from . import UserRole

class UserLogin(BaseModel):
  email: str
  password: str

class UserCreate(UserLogin):
  handle: str
  birthday: date
  role: UserRole

class UserQuery(BaseModel):
  name: Optional[str]
  handle: Optional[str]
  about_content: Optional[str]

class UserUpdate(BaseModel):
  name: Optional[str] = None
  birthday: Optional[date] = None
  handle: Optional[str] = None
  password: Optional[str] = None
