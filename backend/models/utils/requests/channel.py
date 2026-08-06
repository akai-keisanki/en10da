from datetime import date
from typing import Optional

from pydantic import BaseModel

class ChannelCreate(BaseModel):
  title: str

class ChannelQuery(BaseModel):
  title: Optional[str] = None
  content: Optional[str] = None
  channel_id: Optional[int] = None

class ChannelUpdate(BaseModel):
  title: Optional[str] = None
  content: Optional[str] = None
  channel_id: Optional[int] = None
