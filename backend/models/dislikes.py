from datetime import datetime, timezone
from factory import db

dislikes = db.Table(
    'dislikes',
    db.Column('post_handle', db.String(128), primary_key=True),
    db.Column('post_channel_handle', db.String(128), primary_key=True),
    db.Column('post_author_handle', db.String(128), primary_key=True),

    db.Column('user_handle', db.String(128), db.ForeignKey('users.handle'), primary_key=True),

    db.Column('creation_datetime', db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)),

    db.ForeignKeyConstraint(
      ['post_handle', 'post_channel_handle', 'post_author_handle'],
      ['posts.handle', 'posts.channel_handle', 'posts.author_handle'],
    )
  )
