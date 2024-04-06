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
    datetime = Column(DateTime)

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
    
    # isso aqui é ridículo mas fazer oq, pelo menos no grafana da pra associar os dados direitinho, so vai ficar feio aqui
    # vou deixar o mais fiel possivel ao arquivo das planilhas pra ser facil de procurar, por isso a falta de padrao
    question_1 = Column(String(200))
    question_2 = Column(String(200))
    question_3 = Column(String(200))
    question_4 = Column(String(200))
    question_5 = Column(String(200))
    question_6 = Column(String(200))
    question_7 = Column(String(200))
    question_8 = Column(String(200))
    question_9 = Column(String(200))
    question_10 = Column(Integer)
    question_11 = Column(Integer)
    question_12_a = Column(String(200))
    question_12_b = Column(String(200))
    question_12_c = Column(String(200))
    question_13 = Column(String(200))
    question_14_1 = Column(String(200))
    question_14_2 = Column(String(200))
    question_14_3 = Column(String(200))
    question_14_4 = Column(String(200))
    question_14_5 = Column(String(200))
    question_14_6 = Column(String(200))
    question_14_7 = Column(String(200))
    question_14_8 = Column(String(200))
    question_14_9 = Column(String(200))
    question_15 = Column(String(200))
    question_16 = Column(String(200))
    question_17 = Column(String(200))
    question_18 = Column(String(200))
    question_19_1 = Column(String(200))
    question_19_2 = Column(String(200))
    question_19_3 = Column(String(200))
    question_19_4 = Column(String(200))
    question_19_5 = Column(String(200))
    question_19_6 = Column(String(200))
    question_20_1 = Column(String(200))
    question_20_2 = Column(String(200))
    question_20_3 = Column(String(200))
    question_21 = Column(String(200))
    question_22 = Column(String(200))
    question_23_1 = Column(String(200))
    question_23_2 = Column(String(200))
    question_23_3 = Column(String(200))
    question_24_1 = Column(String(200))
    question_24_2 = Column(String(200))
    question_24_3 = Column(String(200))
    question_24_4 = Column(String(200))
    question_25_1 = Column(String(200))
    question_25_2 = Column(String(200))
    question_25_3 = Column(String(200))
    question_25_4 = Column(String(200))
    question_26_1 = Column(String(200))
    question_26_2 = Column(String(200))
    question_26_3 = Column(String(200))
    question_27 = Column(String(200))
    question_28 = Column(String(200))
    question_29 = Column(String(200))
    question_30 = Column(String(200))
    question_31 = Column(String(200))
    question_32 = Column(String(200))
    question_33 = Column(String(200))
    question_34 = Column(String(200))
    question_35 = Column(String(200))
    question_36 = Column(String(200))
    question_37 = Column(String(200))
    question_38 = Column(String(200))
    question_39 = Column(String(200))
    question_40 = Column(String(200))
    question_41 = Column(String(400))
    question_42 = Column(String(200))
    question_43 = Column(String(200))
    observation = Column(String(200))
    
    upload_id = Column(Integer, ForeignKey("uploads.id"))
    residents = relationship('Resident', backref='form', cascade='all, delete-orphan')

class Resident(Base):#
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
