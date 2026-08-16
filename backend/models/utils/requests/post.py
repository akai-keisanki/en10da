from datetime import date
from typing import Optional

from pydantic import BaseModel

from .user import UserQuerySum
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

  author_handle: Optional[str] = None
  author_name: Optional[str] = None
  @property
  def author(self) -> Optional[UserQuerySum]:
    if self.author_handle or self.author_name:
      return UserQuerySum(handle=self.author_handle, name=self.author_name)
    return None

  channel_handle: Optional[str] = None
  channel_name: Optional[str] = None
  @property
  def channel(self) -> Optional[ChannelQuerySum]:
    if self.channel_handle or self.channel_name:
      return ChannelQuerySum(handle=self.channel_handle, name=self.channel_name)
    return None

class PostUpdate(BaseModel):
  handle: Optional[str] = None
  title: Optional[str] = None
  content: Optional[str] = None
  channel: Optional[ChannelSum] = None
