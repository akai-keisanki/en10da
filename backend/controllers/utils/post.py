from factory import db
from models import Post, User, Channel
from models.utils.requests.post import PostCreate, PostQuery, PostUpdate
from models.utils.responses import DefaultResp
from models.utils.responses.post import PostQueryResp
from . import APIError
from . import user, channel

def owns_post(user: User, post: Post) -> bool:
  return post.author == user or user.is_moderator(user)

def create_post(user: User, data: PostCreate) -> DefaultResp:
  chn = channel.get_channel_by_path(user.handle, data.channel.handle)
  data = data.model_dump()
  data.pop('channel')
  pst = Post(author=user, channel=chn, **data)
  db.session.add(pst)
  db.session.commit()
  return DefaultResp(msg='Post created successfully!')

def get_post(id: int) -> Post:
  pst = db.session.get(Post, id)
  if not pst:
    raise APIError('Post not found', 404)
  return pst

def get_post_by_path(user_handle: str, channel_handle: str, post_handle: str) -> Post:
  pst = db.session.scalars(
    db.select(Post)
    .join(User).join(Channel)
    .where(db.and_(
      User.handle == user_handle,
      Channel.handle == channel_handle,
      Post.handle == post_handle
    ))
  ).first()
  if not pst:
    raise APIError('Post not found', 404)
  return pst

def query_posts(data: PostQuery) -> PostQueryResp:
  query = db.select(Post)
  conds = []
  joined = False
  if data.handle:
    conds.append(Post.handle.icontains(data.handle))
  if data.title:
    conds.append(Post.title.icontains(data.title))
  if data.content:
    for cw in content.split():
      conds.append(Post.content.icontains(cw))
  if data.author:
    query.join(User)
    joined = True
    if data.author_handle:
      conds.append(User.handle.icontains(data.author_handle))
    if data.author_name:
      conds.append(User.name.icontains(data.author_name))
  if data.channel:
    query.join(Channel)
    joined = True
    if data.channel_handle:
      conds.append(Channel.handle.icontains(data.channel_handle))
    if data.channel_name:
      conds.append(Channel.name.icontains(data.channel_name))
  query = query.where(db.and_(*conds))
  if joined:
    query = query.distinct()
  return PostQueryResp(posts=db.session.scalars(query).all())

def update_post(user: User, pst: Post, data: PostUpdate) -> DefaultResp:
  if not owns_post(user, pst):
    raise APIError("Forbidden operation with unauthoral post.", 403)
  ...
  return DefaultResp(msg='Post updated successfully!')

def delete_post(user: User, pst: Post) -> DefaultResp:
  if not owns_post(user, pst):
    raise APIError("Forbidden operation with unauthoral post.", 403)
  if pst.handle == "sobre":
    raise APIError("Cannot delete the default channel \"sobre\" post.", 403)
  ...
  return DefaultResp(msg='Post deleted successfully!')
