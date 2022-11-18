from pydantic import BaseModel


class UserRegister(BaseModel):
    fullname: str
    username: str
    password: str


class LoginVM(BaseModel):
    username: str
    password: str
