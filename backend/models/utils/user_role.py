from enum import Enum

class UserPerm(Enum):
  POST = 0b0000_0001
  LESSON = 0b0000_0010
  CLASS = 0b0000_0100
  FOLLOW = 0b0000_1000
  READLIST = 0b0001_0000
  MODERATE = 0b0100_0000
  ADMIN = 0b1000_0000

  @classmethod
  def check(cls, mask: int, perm: UserPerm) -> bool:
    return mask & perm.value != 0

  @classmethod
  def check_n(cls, mask: int, perms: list[UserPerm]) -> bool:
    for perm in perms:
      if not cls.check(mask, perm):
        return False
    return True

  @classmethod
  def join(cls, mask: int, perm) -> int:
    mask |= perm.value
    return mask

  @classmethod
  def join_n(cls, perms: list[UserPerm], mask: int = 0) -> int:
    for perm in perms:
      mask = cls.join(mask, perm)
    return mask

class UserRole(Enum):
  STUDENT = 1
  POSTER = 2
  TEACHER = 3
  MODERATOR = 19
  ADMIN = 20

  permissions = {
      STUDENT: [UserPerm.FOLLOW, UserPerm.READLIST]
      POSTER: [UserPerm.POST]
      TEACHER: [UserPerm.POST, UserPerm.LESSON, UserPerm.CLASS]
      MODERATOR: [UserPerm.MODERATE]
      ADMIN: list(UserPerm)
    }

  @classmethod
  def from_int(cls, id: int) -> UserRole:
    for role in cls:
      if role.value == id:
        return role
    raise ValueError("Role value was not found.")

  @classmethod
  def from_string(cls, name: str) -> UserRole:
    for role in cls:
      if role.name == name:
        return role
    raise ValueError("Role name was not found.")

  def get_perm_mask(self) -> int:
    return UserPerm.join_n(self.permissions[self])
