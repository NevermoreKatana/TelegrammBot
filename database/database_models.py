from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    name = Column(String)
    surname = Column(String)
    time = Column(DateTime)


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    time = Column(DateTime)
    user_id = Column(BigInteger)


class Greeting(Base):
    __tablename__ = 'greetings'
    id = Column(Integer, primary_key=True)
    character_name = Column(String, ForeignKey('characters.name'), nullable=False)
    greeting_text = Column(String, nullable=False)


class UserRequest(Base):
    __tablename__ = 'user_request'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    request = Column(String, nullable=False)
    response = Column(String)


class Prompt(Base):
    __tablename__ = 'prompts'
    id = Column(Integer, primary_key=True)
    prompt = Column(String)
    character_name = Column(String)
