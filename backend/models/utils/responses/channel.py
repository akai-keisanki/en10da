from datetime import datetime

from pydantic import BaseModel

from . import ORMBase

class ChannelRespSum(ORMBase):
  name: str
