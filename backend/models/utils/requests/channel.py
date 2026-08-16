from datetime import date
from typing import Optional

from pydantic import BaseModel

class ChannelSum(BaseModel):
  handle: str

class ChannelCreate(ChannelSum):
  name: str

class ChannelQuerySum(BaseModel):
  handle: Optional[str] = None
  name: Optional[str] = None

class ChannelQuery(ChannelQuerySum):
  about_content: Optional[str] = None

  author_handle: Optional[str] = None
  author_name: Optional[str] = None
  @property
  def author(self) -> Optional[UserQuerySum]:
    if self.author_handle or self.author_name:
      return UserQuerySum(handle=self.author_handle, name=self.author_name)
    return None

class ChannelUpdate(BaseModel):
  handle: Optional[str] = None
  name: Optional[str] = None
