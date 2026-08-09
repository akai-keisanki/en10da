from datetime import datetime, date

from pydantic import BaseModel, ConfigDict, field_validator

class ORMBase(BaseModel):
  id: int
  @field_validator("*")
  @classmethod
  def val_dates(cls, obj):
      if (isinstance(obj, datetime)):
          return datetime.strftime(obj, '%Y-%m-%d %H:%M:%S')
      elif (isinstance(obj, date)):
          return datetime.strftime(obj, '%Y-%m-%d')
      else:
        return obj
  model_config = ConfigDict(from_attributes=True)

class DefaultResp(BaseModel):
  msg: str

