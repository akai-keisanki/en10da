from os import path, environ
from secrets import token_hex
from dotenv import load_dotenv

from flask import Flask

load_dotenv()

BASE_DIR: str = path.abspath(path.dirname('__file__'))

class Config:
  SECRET_KEY: str = environ.get('SECRET_KEY', token_hex())
  DEBUG: bool = environ.get('DEBUG', True)
  ADM_EMAIL: str = environ.get('EMAIL')
  APP_TITLE: str = environ.get('APP_TITLE', 'En10da')

  SQLALCHEMY_DATABASE_URI: str = environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + path.join(BASE_DIR, environ.get('DATABASE_PATH', 'app.db')))
  SQLALCHEMY_TRACK_MODIFICATIONS: bool = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)

  SMTP_SERVER: str = environ.get('SMTP_SERVER', 'smtp.gmail.com')
  SMTP_PORT: int = environ.get('SMTP_PORT', 587)
  SMTP_USERNAME: str = environ.get('EMAIL')
  SMTP_PASSWORD: str = environ.get('SMTP_PASSWORD')
  SMTP_SENDER: str = environ.get('EMAIL')

  def init_app(self, app: Flask) -> None:
    app.config.from_object(self)
