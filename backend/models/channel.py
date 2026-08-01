from factory import db

class Channel(db.Model):
  __tablename__ = 'channels'

  id = db.Column(db.Integer, primary_key=True)

  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(512), nullable=False, default='')
  
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  author = db.relationship('User', back_populates='channels')

  posts = db.relationship('Post', back_populates='channel')
