from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates

from .likes import likes
from .dislikes import dislikes
from factory import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)

  email = db.Column(db.String(128), nullable=False)
  @validates('email')
  def validate_email(self, key, value):
    value = value.strip().lower()
    if not re.match('[a-z0-9_.]+@[a-z0-9_.]', value):
      raise ValueError('Invalid email.')
    return value

  password_hash = db.Column(db.Text, nullable=True)
  def set_password (self, password: str) -> None:
    self.password_hash = generate_password_hash(password)
  def check_password (self, password: str) -> bool:
    return check_password_hash(self.password_hash, password)

  handle = db.Column(db.String(64), nullable=False, unique=True)

  role = db.Column(db.String(32), nullable=False)

  name = db.Column(db.String(64), nullable=False)
  birthday = db.Column(db.Date)

  creation_datetime = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow().date())

  posts = db.relationship('Post', back_populates='author')
  channels = db.relationship('Channel', back_populates='author')

  liked_posts = db.relationship('Post', secondary=likes, back_populates='likes')
  disliked_posts = db.relationship('Post', secondary=dislikes, back_populates='dislikes')

  readlists = db.relationship('Readlist', back_populates='author')
