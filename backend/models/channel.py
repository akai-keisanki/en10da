from datetime import datetime

from factory import db

class Channel(db.Model):
  __tablename__ = 'channels'

  id = db.Column(db.Integer, primary_key=True)

  name = db.Column(db.String(128), nullable=False)

  creation_datetime = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow().date())
  
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  author = db.relationship('User', back_populates='channels')

  posts = db.relationship('Post', back_populates='channel')

  like_count = db.Column(db.Integer, nullable=False, default=0)
  dislike_count = db.Column(db.Integer, nullable=False, default=0)
