from pydantic import BaseModel

from . import ORMBase

class UserLoginResp(BaseModel):
  access_token: str

class UserRespSum(ORMBase):
  handle: str

class UserResp(UserRespSum):
  name: str
