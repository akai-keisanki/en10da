from flask import Blueprint, request
from spectree import Response

from factory import api
from models import User
from models.utils.responses import DefaultResp
from models.utils.requests.user import UserCreate, UserUpdate, UserLogin, UserEmailCodeRequest, UserEmailLogin
from models.utils.responses.user import UserLoginResp, UserResp, UserQueryResp, UserPrivResp, UserRoleListResp
from .utils import wrap_resp, req_perms, BA_SEC
from .utils.user import create_user, make_user_login, make_user_login_by_email_code, get_logged_user, get_user_by_handle, query_users, update_user, delete_user, send_user_email_code, list_user_roles

user_bp = Blueprint('user_controllers', __name__, url_prefix='/user')

@user_bp.post('/logon')
@api.validate(json=UserCreate, resp=Response(HTTP_200=DefaultResp), tags=['user'])
@wrap_resp(def_code=201)
def user_logon():
  return create_user(UserCreate.model_validate(request.get_json()))

@user_bp.post('/login')
@api.validate(json=UserLogin, resp=Response(HTTP_200=UserLoginResp, HTTP_401=DefaultResp), tags=['user'])
@wrap_resp(def_code=201)
def user_login():
  return make_user_login(UserLogin.model_validate(request.get_json()))

@user_bp.post('/request-email-code')
@api.validate(json=UserEmailCodeRequest, resp=Response(HTTP_200=DefaultResp), tags=['user'])
@wrap_resp(def_code=201)
def user_request_email_code():
  return send_user_email_code(UserEmailCodeRequest.model_validate(request.get_json()))

@user_bp.post('/login/email')
@api.validate(json=UserEmailLogin, resp=Response(HTTP_200=UserLoginResp, HTTP_401=DefaultResp), tags=['user'])
@wrap_resp(def_code=201)
def user_login_email():
  return make_user_login_by_email_code(UserEmailLogin.model_validate(request.get_json()))

@user_bp.get('/')
@api.validate(resp=Response(HTTP_200=UserPrivResp), tags=['user'], security=BA_SEC)
@wrap_resp()
@req_perms()
def user_get(user: User):
  return UserPrivResp.model_validate(user)

@user_bp.get('/<string:handle>')
@api.validate(resp=Response(HTTP_200=UserResp), tags=['user'])
@wrap_resp()
def user_handle_get(handle: str):
  return UserResp.model_validate(get_user_by_handle(handle))

@user_bp.post('/')
@api.validate(json=UserUpdate, resp=Response(HTTP_200=DefaultResp), tags=['user'], security=BA_SEC)
@wrap_resp(def_code=201)
@req_perms()
def user_post(user: User):
  return update_user(user, UserUpdate.model_validate(request.get_json()))

@user_db.get('/roles')
@api.validate(resp=Response(HTTP_200=UserRoleListResp), tags=['user'])
@wrap_resp()
def user_get():
  return UserRoleListResp(list_user_roles())
