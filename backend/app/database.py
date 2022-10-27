from base64 import encode
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typer import echo

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# PyMySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/46comp1031"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    encoding="utf-8",
    echo=True,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
