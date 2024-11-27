from sqlalchemy import Column, String, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
from infrastructure.database.session import Base
import uuid
import enum


class UserRole(enum.Enum):
    admin = 'admin'
    user = 'user'


class User(Base):
    __tablename__ = 'users'

    user_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     index=True,
                     unique=True,
                     nullable=False,
                     default=uuid.uuid4)
    username = Column(String, unique=True)
    name = Column(String,nullable=False)
    age = Column(Integer, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, unique=True)
    role = Column(Enum(UserRole), default=UserRole.user)
