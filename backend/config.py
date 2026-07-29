from os import path, environ
from secrets import token_hex
from dotenv import load_dotenv

from flask import Flask

load_dotenv()

BASE_DIR: str = path.abspath(path.dirname('__file__'))

class Config:
  SECRET_KEY: str = environ.get('SECRET_KEY', token_hex())
  ADM_EMAIL: str = environ.get('EMAIL', 'admin@example.com')
  APP_TITLE: str = environ.get('APP_TITLE', 'En10da')
  SQLALCHEMY_DATABASE_URI: str = environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + path.join(BASE_DIR, environ.get('DATABASE_PATH', 'app.py')))
  SQLALCHEMY_TRACK_MODIFICATIONS: bool = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
  DEBUG: bool = environ.get('DEBUG', True)

  def init_app(self, app: Flask) -> None:
    app.config.from_object(self)
