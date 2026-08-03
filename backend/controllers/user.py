from flask import Blueprint
from spectree import Response

from factory import api
from .utils import wrap_resp
from models import User
from models.utils.requests import UserLoginJSON
from models.utils.responses import DefaultResp, UserLoginResp

user_bp = Blueprint('user_controllers', __name__, url_prefix='/user')

@user_bp.post('/login')
@api.validate(json=UserLoginJSON, resp=Response(HTTP_200=DefaultResp), tags=['user'])
@wrap_resp
def login():
  username = request.json.
  return 'Unnavailable :/', 500
