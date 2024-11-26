from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str


class Register(BaseModel):
    username: str
    email: str
    password: str
