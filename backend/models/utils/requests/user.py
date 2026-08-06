from datetime import date
from typing import Optional

from pydantic import BaseModel

from models.utils import UserRole

class UserLogin(BaseModel):
  email: str
  password: str

class UserCreate(UserLogin):
  handle: str
  birthday: date
  role: UserRole

class UserQuery(BaseModel):
  name: Optional[str] = None
  handle: Optional[str] = None
  about_content: Optional[str] = None

class UserUpdate(BaseModel):
  name: Optional[str] = None
  birthday: Optional[date] = None
  handle: Optional[str] = None
  password: Optional[str] = None
