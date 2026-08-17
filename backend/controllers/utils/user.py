from datetime import datetime
from random import randint
from secrets import token_urlsafe
from os import path

from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

from config import BASE_DIR
from factory import db
from models import User, Post, Channel
from models.utils import UserRole, UserPerm
from models.utils.requests.user import UserCreate, UserQuery, UserUpdate, UserLogin, UserEmailCodeRequest, UserEmailLogin
from models.utils.requests.channel import ChannelCreate
from models.utils.responses import DefaultResp
from models.utils.responses.user import UserLoginResp, UserQueryResp
from . import APIError, send_email
from . import channel

def check_if_moderator(user: User) -> bool:
  return UserRole.from_int(user.role).get_perm_mask() & UserPerm.MODERATE.value == UserPerm.MODERATE.value

def list_user_roles() -> list[UserRoles]:
  return UserRole.get_available()

def create_user(data: UserCreate) -> DefaultResp:
  if data.role not in list_user_roles():
    raise APIError('Forbidden role assignment.', 403)
  user = User(name=data.handle, **data.model_dump())
  db.session.add(user)
  channel.create_channel(user, ChannelCreate(handle=user.handle, name=user.name))
  db.session.commit()
  return DefaultResp(msg='User created succesfully!')

def get_logged_user() -> User:
  return db.session.get(User, int(get_jwt_identity()))
  
def get_user(id: int) -> User:
  user = db.session.get(User, id)
  if not user:
    raise APIError('User not found', 404)
  return user

def get_user_by_handle(handle: str) -> User:
  user = db.session.scalars(db.select(User).where(User.handle == handle)).first()
  if not user:
    raise APIError('User not found', 404)
  return user

def query_users(data: UserQuery) -> UserQueryResp:
  query = db.select(User)
  conds = []
  joined = False
  if data.handle:
    conds.append(User.handle.icontains(data.handle))
  if data.name:
    conds.append(User.name.icontains(data.name))
  if data.about_content:
    query.join(Post)
    query.join(Channel)
    joined = True
    conds.append(Post.handle == 'sobre')
    conds.append(Channel.handle == User.handle)
    conds.append(Post.channel_id == Channel.id)
    for aw in about_content.split():
      conds.append(Post.content.icontains(aw))
  query = query.where(db.and_(*conds))
  if joined:
    query = query.distinct()
  return UserQueryResp(users=db.session.scalars(query).all())
  
def update_user(user: User, data: UserUpdate) -> DefaultResp:
  password_updated = False
  password = data.password
  data = data.model_dump()
  data.pop('password')
  for k, v in data.items():
    if v is not None:
      setattr(user, k, v)
  if password:
    user.set_password(password)
    password_updated = True
  db.session.commit()
  return DefaultResp(msg='User updated successfully!' + (' + password updated' if password_updated else ''))

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
  send_email(subject='Código de email',
             body=open(path.join(BASE_DIR, 'emails/email_code.html'), 'r').read().replace('{user.email_code_expiration_datetime}', user.email_code_expiration_datetime),
             html=True,
             address=user.email)
  db.session.commit()
  return DefaultResp(msg='Email sent successfully!')

def make_user_login_by_email_code(data: UserEmailLogin) -> UserLoginResp:
  user = get_user_by_handle(data.handle)
  if not user.check_email_code(data.email_code):
    raise APIError('Wrong or invalid email code.', 401)
  return UserLoginResp(access_token=make_user_access_token(user))
