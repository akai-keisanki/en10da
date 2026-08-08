from datetime import datetime, timezone

from factory import db
from .likes import likes
from .dislikes import dislikes
from .readlist_posts import readlist_posts

class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True)

  handle = db.Column(db.String(128), nullable=False, unique=True)
  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text, nullable=False)

  creation_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

  author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  author = db.relationship('User', back_populates='posts')

  channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False, index=True)
  channel = db.relationship('Channel', back_populates='posts')

  likes = db.relationship('User', secondary=likes, back_populates='liked_posts')
  dislikes = db.relationship('User', secondary=dislikes, back_populates='disliked_posts')

  like_count = db.Column(db.Integer, nullable=False, default=0)
  dislike_count = db.Column(db.Integer, nullable=False, default=0)

  readlists = db.relationship('Readlist', secondary=readlist_posts, back_populates='posts')

  __table_args__ = (
    db.UniqueConstraint('channel_id', 'handle', name='uq_handle'),
  )
