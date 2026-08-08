from datetime import datetime
from random import randint
from secrets import token_urlsafe

from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

from factory import db
from models import User
from models.utils import UserRole, UserPerm
from models.utils.requests.user import UserCreate, UserQuery, UserUpdate, UserLogin, UserEmailCodeRequest, UserEmailLogin
from models.utils.responses import DefaultResp
from models.utils.responses.user import UserLoginResp, UserQueryResp
from . import APIError, send_email

def check_if_moderator(user: User) -> bool:
  return UserRole.from_int(user.role).get_perm_mask() & UserPerm.MODERATE.value == UserPerm.MODERATE.value

def create_user(data: UserCreate) -> DefaultResp:
  user = User(name=data.handle, **data.model_dump())
  db.session.add(user)
  db.session.commit()
  return DefaultResp(msg='User created succesfully!')

def get_logged_user() -> User:
  return User.query.filter_by(id=int(get_jwt_identity())).first()
  
def get_user(id: int) -> User:
  user = User.query.filter_by(id=id).first()
  if not user:
    raise APIError('User not found', 404)
  return user

def get_user_by_handle(handle: str) -> User:
  user = User.query.filter_by(handle=handle).first()
  if not user:
    raise APIError('User not found', 404)
  return user

def query_users(data: UserQuery) -> UserQueryResp:
  ...
  
def update_user(user: User, data: UserUpdate) -> DefaultResp:
  ...

def delete_user(user: User) -> DefaultResp:
  ...

def make_user_access_token(user: User) -> str:
  return create_access_token(identity=str(user.id))

def make_user_login(data: UserLogin) -> UserLoginResp:
  user = get_user_by_handle(data.handle)
  if not user.check_password(data.password):
    raise APIError('Wrong or unset password.', 401)
  return UserLoginResp(access_token=make_user_access_token(user))

def send_user_email_code(data: UserEmailCodeRequest) -> DefaultResp:
  user = get_user_by_handle(data.handle)
  if user.email != data.email:
    raise APIError('Wrong email.', 401)
  if user.email_code_is_valid():
    raise APIError('There was already sent a valid email code.', 409)
  code = token_urlsafe(randint(128, 256))
  user.set_email_code(code)
  send_email(subject='En10da email code',
             body=f'If you don\'t have an En10da account, please ignore this email.\nGenerated code: {code}\nExpires at {user.email_code_expiration_datetime} UTC or at use.',
             address=user.email)
  db.session.commit()
  return DefaultResp(msg='Email sent successfully!')

def make_user_login_by_email_code(data: UserEmailLogin) -> UserLoginResp:
  user = get_user_by_handle(data.handle)
  if not user.check_email_code(data.email_code):
    raise APIError('Wrong or invalid email code.', 401)
  return UserLoginResp(access_token=make_user_access_token(user))


