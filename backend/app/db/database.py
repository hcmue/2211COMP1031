from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = '''
mysql+pymysql://root:@localhost/2211comp103102'''

engine = create_engine(
    DATABASE_URL,
    encoding="utf-8",
    echo=True,
)
Base = declarative_base()
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
