from datetime import date
from typing import Optional

from pydantic import BaseModel

from models.utils import UserRole

class UserCreate(BaseModel):
  handle: str
  email: str
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

class UserLogin(BaseModel):
  handle: str
  password: str

class UserEmailCodeRequest(BaseModel):
  handle: str
  email: str

class UserEmailLogin(BaseModel):
  handle: str
  email_code: str
