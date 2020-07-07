# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
import sqlalchemy as db
from utils.db import Base


class User(Base):
    __tablename__ = 'users'
    id = db.Column('id', db.String, primary_key=True)
    name = db.Column('name', db.String)
    email = db.Column('email', db.String, index=True, unique=True)
    # updatedBy = db.Column('updated_by', db.String)
    # updatedOn = db.Column('updated_on', db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.email
