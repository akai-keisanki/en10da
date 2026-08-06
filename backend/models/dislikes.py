from factory import db

dislikes = db.Table(
    'dislikes',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False),
    db.Column('creation_datetime', db.DateTime, nullable=False, default=lambda: datetime.utcnow().date())
  )
