from datetime import datetime, timezone
import re

from sqlalchemy.orm import validates

from factory import db
from .likes import likes
from .dislikes import dislikes
from .readlist_posts import readlist_posts

class Post(db.Model):
  __tablename__ = 'posts'

  handle = db.Column(db.String(128), primary_key=True)
  @validates('handle')
  def validate_handle(self, key, value):
    value = value.strip().lower()
    if not re.match('[a-zA-Z1-9_-]+', value):
      raise ValueError('Invalid handle.')
    return value
  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text, nullable=False, default='')

  creation_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

  author_handle = db.Column(db.String(128), db.ForeignKey('users.handle'), primary_key=True)
  author = db.relationship('User', back_populates='posts', overlaps='channel,posts', viewonly=True)

  channel_handle = db.Column(db.String(128), primary_key=True)
  channel = db.relationship('Channel', back_populates='posts', overlaps='author,posts')

  likes = db.relationship('User', secondary=likes, back_populates='liked_posts')
  dislikes = db.relationship('User', secondary=dislikes, back_populates='disliked_posts')

  like_count = db.Column(db.Integer, nullable=False, default=0)
  dislike_count = db.Column(db.Integer, nullable=False, default=0)

  readlists = db.relationship('Readlist', secondary=readlist_posts, back_populates='posts')

  __table_args__ = (
    db.ForeignKeyConstraint(
      ['channel_handle', 'author_handle'],
      ['channels.handle', 'channels.author_handle']
    ),
  )
