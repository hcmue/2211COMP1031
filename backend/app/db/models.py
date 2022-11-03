from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(150), unique=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(150))
    is_active = Column(Boolean, default=True)
