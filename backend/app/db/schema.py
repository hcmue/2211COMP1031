from sqlalchemy import Integer, Column, String, Boolean
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,  index=True, autoincrement=True)
    fullname = Column(String(150))
    username = Column(String(50), unique=True, index=True)
    password = Column(String(150))
    is_active = Column(Boolean, default=True)
