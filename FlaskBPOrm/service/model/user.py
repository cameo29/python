'''
Created on 2017. 11. 8.
user table
'''
# database column에 대한 타입 import
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship # 세부쿼리 수행
from service.model import Base

class User(Base):
    # 테이블명
    __tablename__ = 'users2'
    # 컬럼
    id          = Column(Integer   , primary_key=True) 
    username    = Column(String(50), unique=True)
    email       = Column(String(50), unique=False)
    password    = Column(String(50), unique=False)
    # 생성자
    def __init__(self, username, email, password):
        self.username   = username
        self.email      = email
        self.password   = password
    # 기타
    def __repr__(self):
        value = "<User %r %r>" % (self.username, self.email)
        print(value)
        return value
    
