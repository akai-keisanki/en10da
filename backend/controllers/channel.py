from flask import Blueprint, request
from spectree import Response

from factory import api
from models import User
from models.utils import UserPerm
from models.utils.requests.channel import ChannelCreate, ChannelQuery
from models.utils.responses import DefaultResp
from models.utils.responses.channel import ChannelResp, ChannelQueryResp
from .utils import wrap_resp, req_perms, BA_SEC
from .utils.channel import create_channel, get_channel_by_path
from .utils.user import get_logged_user

channel_bp = Blueprint('channel_controllers', __name__, url_prefix='/channel')

@channel_bp.post('/')
@api.validate(json=ChannelCreate, resp=Response(HTTP_200=DefaultResp), tags=['channel'], security=BA_SEC)
@req_perms([UserPerm.POST])
@wrap_resp(def_code=201)
def channel_create(user: User, json: ChannelCreate):
  return create_channel(user, json)

@channel_bp.get('/<string:user_handle>/<string:channel_handle>')
@api.validate(resp=Response(HTTP_200=ChannelResp), tags=['channel'])
@wrap_resp()
def channel_get(user_handle: str, channel_handle: str):
  return ChannelResp.model_validate(get_channel_by_path(user_handle, channel_handle))
