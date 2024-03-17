from sqlalchemy import Column, Integer, String

from src.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    age = Column(Integer)
    email = Column(String(32), unique=True)
    password = Column(String(80))
