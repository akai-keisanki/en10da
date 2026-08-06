from factory import db
from models import Post
from models.utils.requests.post import PostCreate, PostQuery, PostUpdate
from . import APIError
from .user import is_moderator

def owns_post(user: User, post: Post) -> bool:
  return post.author == user or is_moderator(user)

def create_post(user: User, data: PostCreate) -> Post:
  ...

def get_post(id: int) -> Post:
  ...

def query_posts(data: PostQuery) -> list[Post]:
  ...

def update_post(user: User, post: Post, data: PostUpdate) -> None:
  if not owns_post(user, post):
    raise APIError("Forbidden operation with unauthoral post.", 403)
  ...

def delete_post(user: User, post: Post) -> None:
  if not owns_post(user, post):
    raise APIError("Forbidden operation with unauthoral post.", 403)
  ...
