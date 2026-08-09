from pydantic import BaseModel

from models.utils import UserRole
from . import ORMBase

class UserLoginResp(BaseModel):
  access_token: str

class UserResp(ORMBase):
  handle: str
  name: str

class UserPrivResp(UserResp):
  email: str

class UserQueryResp(BaseModel):
  users: list[UserResp]

class UserRoleList(BaseModel):
  user_roles: list[UserRole]
