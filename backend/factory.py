from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from spectree import SpecTree

from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
api = SpecTree('flask', path='docs', security_schemes=[{'name': 'BearerAuth', 'data': {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}}])

def create_app(name) -> Flask:
  app = Flask(name)

  Config().init_app(app)

  jwt.init_app(app)

  db.init_app(app)
  from models import User
  migrate.init_app(app)

  from controllers import user_bp

  app.register_blueprint(user_bp)

  CORS(app, resources={"/*": {"origins": "*"}})

  return app
