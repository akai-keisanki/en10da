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
  about_content: Optional[str] = None

class ChannelQuery(ChannelQuerySum):
  user: Optional[UserQuery] = None

class ChannelUpdate(BaseModel):
  handle: Optional[str] = None
  name: Optional[str] = None
