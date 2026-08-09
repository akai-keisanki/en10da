from datetime import datetime

from pydantic import BaseModel

from . import ORMBase
from .user import UserResp
from .channel import ChannelResp0

class PostRespSum(ORMBase):
  handle: str
  title: str
  creation_datetime: datetime
  like_count: int
  dislike_count: int
  author: UserResp
  channel: ChannelResp0

class PostResp(PostRespSum):
  content: str

class PostQueryResp(BaseModel):
  posts: list[PostRespSum]
