from datetime import datetime, timezone
from factory import db

readlist_posts = db.Table(
    'readlist_posts',
    db.Column('readlist_handle', db.String(128), primary_key=True),
    db.Column('readlist_author_handle', db.String(128), primary_key=True),

    db.Column('post_handle', db.String(128), primary_key=True),
    db.Column('post_channel_handle', db.String(128), primary_key=True),
    db.Column('post_author_handle', db.String(128), primary_key=True),

    db.Column('creation_datetime', db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)),

    db.ForeignKeyConstraint(
      ['readlist_handle', 'readlist_author_handle'],
      ['readlists.handle', 'readlists.author_handle']
    ),
    db.ForeignKeyConstraint(
      ['post_handle', 'post_channel_handle', 'post_author_handle'],
      ['posts.handle', 'posts.channel_handle', 'posts.author_handle']
    )
  )
