from datetime import datetime, timezone
from factory import db

likes = db.Table(
    'likes',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False),
    db.Column('creation_datetime', db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
  )
