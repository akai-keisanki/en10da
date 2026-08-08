from datetime import datetime, timezone
from factory import db

readlist_posts = db.Table(
    'readlist_posts',
    db.Column('readlist_id', db.Integer, db.ForeignKey('readlists.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('creation_datetime', db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
  )
