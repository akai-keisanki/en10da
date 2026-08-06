from factory import db
from models import Channel
from models.utils.requests.channel import ChannelCreate, Channel, ChannelUpdate

def create_channel(data: ChannelCreate) -> Channel:
  ...

def get_channel(id: int) -> Channel:
  ...

def query_channels(data: ChannelQuery) -> list[Channel]:
  ...

def update_channel(channel: Channel, data: ChannelUpdate) -> None:
  ...

def delete_channel(channel: Channel) -> None:
  ...
