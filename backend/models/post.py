from factory import db

class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True)

  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text, nullable=False)
