from datetime import datetime

from pydantic import BaseModel

from . import ORMBase
from .user import UserResp

class ChannelResp0(ORMBase):
  handle: str
  name: str

class ChannelResp(ChannelResp0):
  user: UserResp

class ChannelQueryResp(BaseModel):
  channels: list[ChannelResp]
