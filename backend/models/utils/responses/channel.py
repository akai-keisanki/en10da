from datetime import datetime

from pydantic import BaseModel

from . import ORMBase

class ChannelResp(ORMBase):
  handle: str
  title: str

class ChannelQueryResp(BaseModel):
  channels: list[ChannelResp]
