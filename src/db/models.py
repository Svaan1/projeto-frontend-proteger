from sqlalchemy import Column, Integer, String, Date, Double, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    age = Column(Integer)
    email = Column(String(32), unique=True)
    password = Column(String(80))

    uploads = relationship('Upload', backref='user', cascade='all')

class Upload(Base):
    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True)

    filename = Column(String(100), unique=True)
    date = Column(DateTime)

    user_id = Column(Integer, ForeignKey("users.id"))
    forms = relationship('Form', backref='upload', cascade='all, delete-orphan')


class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True)

    date = Column(Date)
    district = Column(String(50))
    address = Column(String(100))
    coord_s = Column(Double)
    coord_w = Column(Double)
    altitude = Column(Integer)
    ivge = Column(Integer)
    ivee = Column(Integer)
    
    # TODO: add the 40 questions to columns later
    # ... 

    upload_id = Column(Integer, ForeignKey("uploads.id"))
    residents = relationship('Resident', backref='form', cascade='all, delete-orphan')

class Resident(Base):
    __tablename__ = "residents"

    id = Column(Integer, primary_key=True)

    sex = Column(String(1))
    age = Column(Integer)
    mobility_restriction = Column(String(100))
    sensory_impairment = Column(String(100))
    mental_disorder = Column(String(100))
    health_injury = Column(String(100))
    education = Column(String(100))

    form_id = Column(Integer, ForeignKey("forms.id"))
