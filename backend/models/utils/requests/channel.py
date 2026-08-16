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

  user_handle: Optional[str] = None
  user_name: Optional[str] = None
  @property
  def user(self) -> Optional[UserQuerySum]:
    if self.user_handle or self.user_name:
      return UserQuerySum(handle=self.user_handle, name=self.user_name)
    return None

class ChannelUpdate(BaseModel):
  handle: Optional[str] = None
  name: Optional[str] = None
