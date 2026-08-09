from factory import db
from models import Channel, User
from models.utils.requests.channel import ChannelCreate, ChannelQuery, ChannelUpdate, ChannelSum
from models.utils.requests.post import PostCreate
from models.utils.responses import DefaultResp
from models.utils.responses.channel import ChannelQueryResp
from . import APIError
from . import user, post

def owns_channel(user: User, channel: Channel) -> bool:
  return channel.author == user or user.is_moderator(user)

def create_channel(user: User, data: ChannelCreate) -> DefaultResp:
  channel = Channel(author=user, **data.model_dump())
  db.session.add(channel)
  post.create_post(user, PostCreate(handle='sobre', title='Sobre', content='', channel=ChannelSum(handle=channel.handle)))
  db.session.commit()
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
  if user.handle == channel.handle:
    raise APIError("Cannot delete the default user channel.", 403)
  db.session.delete(channel)
  db.session.commit()
  return DefaultResp(msg='Channel deleted successfully!')
