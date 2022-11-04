from pydantic import BaseModel


class UserRegister(BaseModel):
    fullname: str
    username: str
    password: str
