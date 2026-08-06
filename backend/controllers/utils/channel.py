from factory import db
from models import Channel
from models.utils.requests.channel import ChannelCreate, Channel, ChannelUpdate
from . import APIError
from .user import is_moderator

def owns_channel(user: User, channel: Channel) -> bool:
  return channel.author == user or is_moderator(user)

def create_channel(user: User, data: ChannelCreate) -> Channel:
  ...

def get_channel(id: int) -> Channel:
  ...

def query_channels(data: ChannelQuery) -> list[Channel]:
  ...

def update_channel(user: User, channel: Channel, data: ChannelUpdate) -> None:
  if not owns_channel(user, channel):
    raise APIError("Forbidden operation with unauthoral channel.", 403)
  ...

def delete_channel(user: User, channel: Channel) -> None:
  if not owns_channel(user, channel):
    raise APIError("Forbidden operation with unauthoral channel.", 403)
  ...
