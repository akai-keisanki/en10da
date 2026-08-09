from flask import Blueprint, request
from spectree import Response

from factory import api
from models import User
from models.utils import UserPerm
from models.utils.requests.post import PostCreate, PostQuery
from models.utils.responses import DefaultResp
from models.utils.responses.post import PostResp, PostQueryResp
from .utils import wrap_resp, req_perms, BA_SEC
from .utils.post import create_post, get_post_by_path
from .utils.user import get_logged_user

post_bp = Blueprint('post_controllers', __name__, url_prefix='/post')

@post_bp.post('/')
@api.validate(json=PostCreate, resp=Response(HTTP_200=DefaultResp), tags=['post'], security=BA_SEC)
@req_perms([UserPerm.POST])
@wrap_resp(def_code=201)
def post_create(user: User):
  return create_post(user, PostCreate.model_validate(request.get_json())).model_dump()

@post_bp.get('/<string:user_handle>/<string:channel_handle>/<string:post_handle>')
@api.validate(resp=Response(HTTP_200=PostResp), tags=['post'])
@wrap_resp()
def post_get(user_handle: str, channel_handle: str, post_handle: str):
  return PostResp.model_validate(get_post_by_path(user_handle, channel_handle, post_handle)).model_dump()

