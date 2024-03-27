from enum import unique

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from database.db import Base
from sqlalchemy.orm import Relationship

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    notes_created = Relationship("Note", back_populates="creator", cascade="all, delete-orphan")


class Note(Base):
    __tablename__ = "notes"
    note_id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    date_created = Column(DateTime)
    creator_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    creator = Relationship("User", back_populates="notes_created")

