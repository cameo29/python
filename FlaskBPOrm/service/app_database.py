'''
Created on 2017. 11. 8.
데이터베이스 초기화 및 작업
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBManager:
    # 전역변수
    __engine      = None
    __session     = None

    # init(self) self 안써도됨
    # dbconnection 유일하기 때문
    @staticmethod
    def init(db_url, db_log_flag=True):
        # 엔진생성
        DBManager.__engine = create_engine(db_url, echo=db_log_flag)
        # 세션생성
        DBManager.__session = scoped_session(sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=DBManager.__engine
            ))
        
        global dao
        dao = DBManager.__session
    
    @staticmethod
    def init_db():
        # create table, table 구조에 대한 import
        from service.model import user
        # table parent = Base
        from service.model import Base
        # create table all
        Base.metadata.create_all(bind=DBManager.__engine)
        
        
dao = None