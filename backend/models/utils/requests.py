from pydantic import BaseModel
from datetime import date

from . import UserRole

class UserLogin(BaseModel):
  email: str
  password: str

class UserCreate(UserLogin)
  name: str
  birthday: date
  role: UserRole
