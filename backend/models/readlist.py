from datetime import datetime
import re

from sqlalchemy.orm import validates

from factory import db
from .readlist_posts import readlist_posts

class Readlist(db.Model):
  __tablename__ = 'readlists'

  handle = db.Column(db.String(128), primary_key=True)
  @validates('handle')
  def validate_handle(self, key, value):
    value = value.strip().lower()
    if not re.match('[a-zA-Z1-9_-]+', value):
      raise ValueError('Invalid handle.')
    return value
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(512), nullable=False, default='')

  creation_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.utcnow().date())

  author_handle = db.Column(db.String(128), db.ForeignKey('users.handle'), primary_key=True)
  author = db.relationship('User', back_populates='readlists')

  posts = db.relationship('Post', secondary=readlist_posts, back_populates='readlists')
