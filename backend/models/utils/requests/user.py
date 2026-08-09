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
  handle: Optional[str] = None
  name: Optional[str] = None
  about_content: Optional[str] = None

class UserUpdate(BaseModel):
  handle: Optional[str] = None
  name: Optional[str] = None
  birthday: Optional[date] = None
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
