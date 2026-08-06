from flask import Blueprint
from spectree import Response

from factory import api
from .utils import wrap_resp

user_bp = Blueprint('user_controllers', __name__, url_prefix='/user')

@user_bp.post('/login')
@api.validate(json=UserLogin, resp=Response(HTTP_200=UserLoginResp, HTTP_401=DefaultResp), tags=['user'])
@wrap_resp
def user_login():
  ... // TODO
  return 'Unnavailable :/', 500

@user_bp.post('/')
@api.validate(json=UserCreate, resp=Response(HTTP_200=DefaultResp), tags=['user'])
@wrap_resp
def user_create():
  ... // TODO
  return 'Unnavailable :/', 500
