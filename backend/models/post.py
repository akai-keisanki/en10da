from datetime import datetime

from factory import db
from .likes import likes
from .readlist_posts import readlist_posts

class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True)

  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text, nullable=False)

  creation_datetime = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow().date())

  author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  author = db.relationship('User', back_populates='posts')

  channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False, index=True)
  channel = db.relationship('Channel', back_populates='posts')

  likes = db.relationship('User', secondary=likes, back_populates='liked_posts')
  readlists = db.relationship('Readlist', secondary=readlist_posts, back_populates='posts')
