from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(150), unique=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(150))
    is_active = Column(Boolean, default=True)


class Loai(Base):

    __tablename__ = "loais"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tenloai = Column(String(150), unique=True, index=True)

    hanghoas = relationship("HangHoa", back_populates="loai")


class HangHoa(Base):

    __tablename__ = "hanghoas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tenhh = Column(String(150), unique=True, index=True)
    dongia = Column(Float)
    maloai = Column(Integer, ForeignKey(
        "loais.id", ondelete="SET NULL", onupdate="CASCADE"))

    loai = relationship("Loai", back_populates="hanghoas")
