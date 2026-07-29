from flask import Flask

from factory import create_app
from config import Config

app: Flask = create_app(__name__)

if __name__ == '__main__':
  app.run(debug = Config.DEBUG)
