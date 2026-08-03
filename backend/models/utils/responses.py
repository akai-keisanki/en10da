from pydantic import BaseModel, ConfigDict

class ORMBase(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)

class DefaultResp(BaseModel):
  msg: str

class UserLoginResp(BaseModel):
  access_token: str
