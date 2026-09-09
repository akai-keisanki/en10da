from datetime import datetime, timezone
import re

from sqlalchemy.orm import validates

from factory import db

class Channel(db.Model):
  __tablename__ = 'channels'

  handle = db.Column(db.String(128), primary_key=True)
  @validates('handle')
  def validate_handle(self, key, value):
    value = value.strip().lower()
    if not re.match('[a-zA-Z1-9_-]+', value):
      raise ValueError('Invalid handle.')
    return value
  name = db.Column(db.String(128), nullable=False)

  creation_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
  
  author_handle = db.Column(db.String(128), db.ForeignKey('users.handle'), primary_key=True)
  author = db.relationship('User', back_populates='channels')

  posts = db.relationship('Post', back_populates='channel', cascade='all, delete-orphan')

  like_count = db.Column(db.Integer, nullable=False, default=0)
  dislike_count = db.Column(db.Integer, nullable=False, default=0)
