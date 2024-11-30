from pydantic import BaseModel
from enum import Enum
from uuid import UUID
from typing import Optional


class UserRole(str, Enum):
    admin = 'admin'
    user = 'user'


class UserResponseSchema(BaseModel):
    user_id: UUID
    username: str
    name: str
    age: int
    email: str
    role: UserRole

    class Config:
        from_attributes = True


class UserRegisterSchema(BaseModel):
    username: str
    name: str
    age: int
    email: str
    password: str
    role: Optional[UserRole] = UserRole.user

    class Config:
        from_attributes = True
