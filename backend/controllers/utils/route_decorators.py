from functools import wraps

from pydantic import BaseModel
from flask import jsonify
from flask_jwt_extended import jwt_required

from models.utils import UserPerm, UserRole
from models.utils.responses import DefaultResp
from models import User
from . import APIError
from .user import get_logged_user

BA_SEC: list[dict[str, list]] = [{'BearerAuth': []}]

class wrap_resp:
  """
  Wraps a response in a json with code automatically
  """

  def __init__(self, def_code=200, def_msg="Undefined response"):
    self.default_code = def_code
    self.default_message = def_msg

  def __call__(self, route_f):
    @wraps(route_f)
    def wrapped_route(*args, **kwargs):
      resp = self.default_message
      code = self.default_code

      try:
        resp = route_f(*args, **kwargs)
      except ValueError as e:
        resp = (f'ValueError', 400)
        print('ValueError')
        print(e)
      except APIError as e:
        resp = (e.msg, e.code)

      if isinstance(resp, tuple):
        resp, code = resp
      if isinstance(resp, BaseModel):
        resp = resp.model_dump()
      if isinstance(resp, str):
        resp = DefaultResp(msg=resp).model_dump()

      return jsonify(resp), code;

    return wrapped_route

class req_perms:
  """
  Require JWT and a list of permissions (optionally).
  """

  def __init__(self, perms: list[UserPerm]=[], let_moderator: bool=False):
    self.perm_mask = UserPerm.join_n(perms)
    self.let_moderator = let_moderator

  def __call__(self, route_f):
    """
    Route wrapper for requiring login and permissions.
    """

    @jwt_required()
    @wraps(route_f)
    def wrapped_route(*args, **kwargs):
      user = get_logged_user()
      if not user:
        return "Logged user was not found.", 404

      user_perm_mask = UserRole.from_int(user.role).get_perm_mask()
      if (user_perm_mask & self.perm_mask != self.perm_mask
          or user_perm_mask & UserPerm.ADMIN.value != UserPerm.ADMIN.value
          or (self.let_moderator and user_perm_mask & UserPerm.MODERATE.value == UserPerm.MODERATE.value)):
        return 'The logged user (\'s role) does\'nt have enough permissions for this action.', 403

      return route_f(user, *args, **kwargs)

    return wrapped_route
