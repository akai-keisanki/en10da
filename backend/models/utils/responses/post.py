from datetime import datetime

from pydantic import BaseModel

from . import ORMBase
from .user import UserRespSum
from .channel import ChannelRespSum

class PostRespSum0(ORMBase):
  name: str
  creation_datetime: datetime
  likes_count: int
  dislikes_count: int
  author: UserRespSum

class PostRespSum(PostRespSum0)
  channel: ChannelRespSum

class PostResp(PostRespSum):
  content: str

class PostQueryResp(BaseModel):
  posts: list[PostRespSum]
