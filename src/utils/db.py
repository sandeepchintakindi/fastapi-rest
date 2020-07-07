from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql+pypostgresql://test_user:Test1234@db.dfftech.com:5432/test_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=False, echo_pool=True, pool_size=10, max_overflow=0, pool_recycle=1
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def db_session():
    session_local = SessionLocal()
    try:
        yield session_local
    finally:
        session_local.close()
