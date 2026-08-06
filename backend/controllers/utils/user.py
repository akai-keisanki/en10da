from factory import db
from models import User
from models.utils.requests.user import UserLogin, UserCreate, UserQuery, UserUpdate

def create_user(data: UserCreate) -> None:
  user = User(**data.model_dump())
  db.session.add(user)
  db.session.commit()

def get_logged_user() -> User:
  return User.query.filter_by(id=int(get_jwt_identity())).first()
  
def get_user(id: int) -> User:
  return User.query.filter_by(id=id).first()

def query_users(data: UserQuery) -> list[User]:
  ...
  
def update_user(user: User, data: UserUpdate)
  ...

def delete_user(user: User) -> None:
  ...
