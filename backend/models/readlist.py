from datetime import datetime

from factory import db
from .readlist_posts import readlist_posts

class Readlist(db.Model):
  __tablename__ = 'readlists'

  id = db.Column(db.Integer, primary_key=True)

  handle = db.Column(db.String(128), nullable=False)
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(512), nullable=False, default='')

  creation_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.utcnow().date())

  author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  author = db.relationship('User', back_populates='readlists')

  posts = db.relationship('Post', secondary=readlist_posts, back_populates='readlists')

  __table_args__ = (
    db.UniqueConstraint('author_id', 'handle', name='uq_handle'),
  )
