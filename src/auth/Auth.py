import sqlalchemy as db
from utils.db import Base


class Auth(Base):
    __tablename__ = 'profile'

    id = db.Column('id', db.String, primary_key=True)
    email = db.Column('email', db.String, index=True, unique=True)
    password = db.Column('password', db.String)

