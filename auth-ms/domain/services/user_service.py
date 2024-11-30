from infrastructure.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from interfaces.api.v1.schemas.user_schema import UserRegisterSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, db: Session, user: UserRegisterSchema):
        created_user = self.repository.create_user(db, user)
        return created_user
