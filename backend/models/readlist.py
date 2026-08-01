from factory import db
from .readlist_posts import readlist_posts

class Readlist(db.Model):
  __tablename__ = 'readlists'

  id = db.Column(db.Integer, primary_key=True)

  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(512), nullable=False, default='')

  author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  author = db.relationship('User', back_populates='readlists')

  posts = db.relationship('Post', secondary=readlist_posts, back_populates='readlists')
