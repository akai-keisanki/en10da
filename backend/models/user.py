from datetime import datetime, timezone, timedelta
import re

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates

from .likes import likes
from .dislikes import dislikes
from factory import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)

  email = db.Column(db.Text, nullable=False)
  @validates('email')
  def validate_email(self, key, value):
    value = value.strip().lower()
    if not re.match('[a-z0-9_.]+@[a-z0-9_.]+', value):
      raise ValueError('Invalid email.')
    return value

  password_hash = db.Column(db.Text, nullable=True)
  def set_password(self, password: str) -> None:
    self.password_hash = generate_password_hash(password)
  def check_password(self, password: str) -> bool:
    if (self.password_hash is not None
        and check_password_hash(self.password_hash, password)):
      self.remove_email_code()
      return True
    return False

  email_code_hash = db.Column(db.Text, nullable=True)
  email_code_expiration_datetime = db.Column(db.DateTime(timezone=True), nullable=True)
  def set_email_code(self, email_code: str) -> None:
    self.email_code_hash = generate_password_hash(email_code)
    self.email_code_expiration_datetime = datetime.now(timezone.utc) + timedelta(minutes=30)
  def remove_email_code(self) -> None:
    self.email_code_hash = None
    self.email_code_expiration_datetime = None
    db.session.commit()
  def email_code_is_valid(self) -> bool:
    if (self.email_code_hash is not None
        and self.email_code_expiration_datetime is not None
        and self.email_code_expiration_datetime.replace(tzinfo=timezone.utc) > datetime.now(timezone.utc)):
      return True
    self.remove_email_code()
    return False
  def check_email_code(self, email_code: str) -> bool:
    if (self.email_code_is_valid()
        and check_password_hash(self.email_code_hash, email_code)):
      self.remove_email_code()
      return True
    return False

  role = db.Column(db.String(32), nullable=False)
  @validates('role')
  def validate_role(self, key, value):
    value = value.strip().lower()
    if value not in list(UserRole):
      raise ValueError('Invalid role.')
    return value

  handle = db.Column(db.String(64), nullable=False, unique=True)
  @validates('handle')
  def validate_handle(self, key, value):
    value = value.strip().lower()
    if not re.match('[a-zA-Z_-]+', value):
      raise ValueError('Invalid handle.')
    return value
  name = db.Column(db.String(64), nullable=False)
  birthday = db.Column(db.Date)

  creation_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

  posts = db.relationship('Post', back_populates='author', cascade='all, delete-orphan')
  channels = db.relationship('Channel', back_populates='author', cascade='all, delete-orphan')

  liked_posts = db.relationship('Post', secondary=likes, back_populates='likes')
  disliked_posts = db.relationship('Post', secondary=dislikes, back_populates='dislikes')

  readlists = db.relationship('Readlist', back_populates='author', cascade='all, delete-orphan')
