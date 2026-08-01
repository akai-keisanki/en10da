from functools import wraps

from flask import jsonify

from models import User
from models.utils import UserPerm
from models.utils.responses import DefaultResp

def wrap_resp(route_f):
  """
  Wraps a response in a json with code automatically
  """

  @wraps(route_f)
  def wrapped_route(*args, **kwargs):
    try:
      resp = route_f(*args, **kwargs)
    except ValueError:
      return "ValueError", 400
    code = 200

    if isinstance(resp, tuple):
      resp, code = resp
    if isinstance(resp, str):
      resp = DefaultResp(message=resp).model_dump()

    return jsonify(resp), code;

  return wrapped_route

class req_perms:
  """
  Require JWT and a list of permissions (optionally).
  """

  def __init__(self, perms: list[UserPerm]):
    self.perm_mask = UserPerm.join_n(self.perms)

  def wrapper(self, route_f):
    """
    Route wrapper for requiring login and permissions.
    """

    @wraps(route_f)
    def wrapped_route(*args, **kwargs):
      user = User.query.filter_by(id=int(get_jwt_identity())).first()
      if not user:
        return "Logged user was not found.", 404

      user_perm_mask = UserRole.from_int(user.role).get_perm_mask()
      if self.perm_mask & user_perm_mask != user_perm_mask:
        return 'The logged user (\'s role) does\'nt have enough permissions for this action.', 403

      return route(user, *args, **kwargs)

    return wrapped_route
