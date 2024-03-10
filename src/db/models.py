from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey

from src.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    age = Column(Integer)
    email = Column(String(32), unique=True)
    password = Column(String(80))
