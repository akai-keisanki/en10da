from os import path
from datetime import datetime

import pandas as pd

from app import app
from factory import db
from config import Config, BASE_DIR
from models import User, Channel, Post

def main():
  with app.app_context():
    users = pd.read_csv('population/user.csv').to_dict(orient='records')
    channels = pd.read_csv('population/channel.csv').to_dict(orient='records')
    posts = pd.read_csv('population/post.csv').to_dict(orient='records')

    for user_data in users:
      if user_data['handle'] == 'en10da':
        user_data['email'] = Config.ADM_EMAIL
      user_data['birthday'] = datetime.strptime(user_data['birthday'], '%Y-%m-%d').date()
      user = User(**user_data)
      db.session.add(user)

    for channel_data in channels:
      channel = Channel(**channel_data)
      db.session.add(channel)

    for post_data in posts:
      content_path = path.join(BASE_DIR, 'population/posts/', post_data['author_handle'] + '_' + post_data['handle'] + '.md')
      post_data['content'] = open(content_path, 'r').read()
      post = Post(**post_data)
      db.session.add(post)

    db.session.commit()

if __name__ == '__main__':
  main()
