from datetime import date
from typing import Optional

from pydantic import BaseModel

class PostCreate(BaseModel):
  title: str
  content: str
  channel_id: int

class PostQuery(BaseModel):
  title: Optional[str]
  content: Optional[str]
  channel_id: Optional[int]

class UserUpdate(BaseModel):
  name: Optional[str] = None
  birthday: Optional[date] = None
  handle: Optional[str] = None
  password: Optional[str] = None
