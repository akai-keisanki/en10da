from factory import db
from models import Channel
from models.utils.requests.channel import ChannelCreate, Channel, ChannelUpdate
from models.utils.responses import DefaultResp
from models.utils.responses.channel import ChannelQueryResp
from . import APIError
from .user import is_moderator

def owns_channel(user: User, channel: Channel) -> bool:
  return channel.author == user or is_moderator(user)

def create_channel(user: User, data: ChannelCreate) -> DefaultResp:
  ...
  return DefaultResp(msg='Channel created successfully!')

def get_channel(id: int) -> Channel:
  channel = Channel.query.filter_by(id=id).first()
  if not channel:
    raise APIError('Channel not found', 404)
  return channel

def get_channel_by_path(user_handle: str, channel_handle: str) -> Channel:
  channel = Channel.query.join(User).filter(User.handle == user_handle,
                                            Channel.handle == channel_handle).first()
  if not channel:
    raise APIError('Channel not found', 404)
  return channel

def query_channels(data: ChannelQuery) -> ChannelQueryResp:
  ...

def update_channel(user: User, channel: Channel, data: ChannelUpdate) -> DefaultResp:
  if not owns_channel(user, channel):
    raise APIError("Forbidden operation with unauthoral channel.", 403)
  ...
  return DefaultResp(msg='Channel updated successfully!')

def delete_channel(user: User, channel: Channel) -> DefaultResp:
  if not owns_channel(user, channel):
    raise APIError("Forbidden operation with unauthoral channel.", 403)
  return DefaultResp(msg='Channel deleted successfully!')
  ...
