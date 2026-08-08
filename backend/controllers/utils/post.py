from factory import db
from models import Post, User, Channel
from models.utils.requests.post import PostCreate, PostQuery, PostUpdate
from models.utils.responses import DefaultResp
from models.utils.responses.post import PostQueryResp
from . import APIError
from .user import is_moderator

def owns_post(user: User, post: Post) -> bool:
  return post.author == user or is_moderator(user)

def create_post(user: User, data: PostCreate) -> DefaultResp:
  ...
  return DefaultResp(msg='Post created successfully!')

def get_post(id: int) -> Post:
  post = Post.query.filter_by(id=id).first()
  if not post:
    raise APIError('Post not found', 404)
  return post

def get_post_by_path(user_handle: str, channel_handle: str, post_handle: str) -> Post:
  post = Post.query.join(User).join(Channel).filter(User.handle == user_handle,
                                                    Channel.handle == channel_handle,
                                                    Post.handle == post_handle).first()
  if not post:
    raise APIError('Post not found', 404)
  return post

def query_posts(data: PostQuery) -> PostQueryResp:
  ...

def update_post(user: User, post: Post, data: PostUpdate) -> DefaultResp:
  if not owns_post(user, post):
    raise APIError("Forbidden operation with unauthoral post.", 403)
  ...
  return DefaultResp(msg='Post updated successfully!')

def delete_post(user: User, post: Post) -> DefaultResp:
  if not owns_post(user, post):
    raise APIError("Forbidden operation with unauthoral post.", 403)
  ...
  return DefaultResp(msg='Post deleted successfully!')
