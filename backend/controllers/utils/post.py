from factory import db
from models import Post
from models.utils.requests.post import PostCreate, PostQuery, PostUpdate

def create_post(data: PostCreate) -> Post:
  ...

def get_post(id: int) -> Post:
  ...

def query_posts(data: PostQuery) -> list[Post]:
  ...

def update_post(post: Post, data: PostUpdate) -> None:
  ...

def delete_post(post: Post) -> None:
  ...
