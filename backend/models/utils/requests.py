from pydantic import BaseModel
from datetime import date

class UserLoginJSON(BaseModel):
  email: str
  password: str
  name: str
  birthday: date

