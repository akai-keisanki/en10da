from pydantic import BaseModel

from . import ORMBase

class UserLoginResp(BaseModel):
  access_token: str

class UserResp(ORMBase):
  handle: str
  name: str

class UserQueryResp(BaseModel):
  users: list[UserResp]
