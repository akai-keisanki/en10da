from factory import db

likes = db.Table(
    'likes',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), unique=True, nullable=False),
    db.Column('user.id', db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    db.Column('creation_datetime', db.DateTime, nullable=False, default=lambda: datetime.utcnow().date())
  )
