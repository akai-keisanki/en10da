from datetime import datetime, timezone

from factory import db

class Channel(db.Model):
  __tablename__ = 'channels'

  id = db.Column(db.Integer, primary_key=True)

  handle = db.Column(db.String(128), nullable=False)
  name = db.Column(db.String(128), nullable=False)

  creation_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
  
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  author = db.relationship('User', back_populates='channels')

  posts = db.relationship('Post', back_populates='channel')

  like_count = db.Column(db.Integer, nullable=False, default=0)
  dislike_count = db.Column(db.Integer, nullable=False, default=0)

  __table_args__ = (
    db.UniqueConstraint('author_id', 'handle', name='uq_handle'),
  )
