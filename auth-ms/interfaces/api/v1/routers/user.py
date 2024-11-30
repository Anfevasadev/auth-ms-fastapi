from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infrastructure.database.session import get_db
from interfaces.api.v1.schemas.user_schema import UserResponseSchema, UserRegisterSchema
from domain.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get("/")
def read_root():
    return {"Hello": "World from user"}


@router.post("/create", response_model=UserResponseSchema)
def create_user(user: UserRegisterSchema, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)
