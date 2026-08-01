from pydantic import BaseModel

class DefaultResp(BaseModel):
  msg: str

class UserLoginResp(BaseModel):
  access_token: str
