from os import path, environ
from secrets import token_hex
from dotenv import load_dotenv

from flask import Flask

load_dotenv()

BASE_DIR: str = path.abspath(path.dirname('__file__'))

TRUTHY_VALS: list[str] = ['true', 'yes', 'on', '1']

class Config:
  EMAIL: str = environ.get('EMAIL')

  SECRET_KEY: str = environ.get('SECRET_KEY', token_hex())
  DEBUG: bool = environ.get('DEBUG', 'true').lower in TRUTHY_VALS
  ADM_EMAIL: str = EMAIL
  APP_TITLE: str = environ.get('APP_TITLE', 'En10da')

  SQLALCHEMY_DATABASE_URI: str = environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + path.join(BASE_DIR, environ.get('DATABASE_PATH', 'app.db')))
  SQLALCHEMY_TRACK_MODIFICATIONS: bool = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'true').lower in TRUTHY_VALS

  SMTP_SERVER: str = environ.get('SMTP_SERVER', 'smtp.gmail.com')
  SMTP_PORT: int = int(environ.get('SMTP_PORT', '587'))
  SMTP_USERNAME: str = EMAIL
  SMTP_PASSWORD: str = environ.get('SMTP_PASSWORD')
  SMTP_SENDER: str = EMAIL

  def init_app(self, app: Flask) -> None:
    app.config.from_object(self)
