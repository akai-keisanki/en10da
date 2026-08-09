from datetime import date
from typing import Optional

from pydantic import BaseModel

from .user import UserQuery
from .channel import ChannelSum, ChannelQuerySum

class PostCreate(BaseModel):
  handle: str
  title: str
  content: str
  channel: ChannelSum

class PostQuery(BaseModel):
  handle: Optional[str] = None
  title: Optional[str] = None
  content: Optional[str] = None
  user: Optional[UserQuery] = None
  channel: Optional[ChannelQuerySum] = None

class PostUpdate(BaseModel):
  handle: Optional[str] = None
  title: Optional[str] = None
  content: Optional[str] = None
  channel: Optional[ChannelSum] = None
