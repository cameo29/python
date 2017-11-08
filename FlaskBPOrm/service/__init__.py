# 플라스크 생성부
import os
from flask import Flask, render_template

##################################################################
# error
# 404
def not_found(error):
    return render_template("404.html"), 404
# 500
def server_error(error):
    return render_template("500.html", err_msg=str(error)), 500
##################################################################
# application
def create_app(config_path='resource/config.cfg'):
    app = Flask(__name__)
### 환경변수 로드(파일에서 로드, 클래스에서 로드) ###
    from service.app_config import WebConfig
    # 클래스로부터 로드
    app.config.from_object(WebConfig)
    app.config.from_pyfile(config_path, silent=True) 
    #올라온 정보를 찍어볼 수 있음
    print_config(app.config.items()) 
### 데이터베이스 처리 ###
    from service.app_database import DBManager
    db_url = "mysql+pymysql://%s:%s@%s/%s?charset=%s" % (app.config['DB_USER'],
                                                          app.config['DB_PWD'],
                                                          app.config['DB_URL'],
                                                          app.config['DB_DATABASE'],
                                                          app.config['DB_CHARSET']
                                                          )
    print(db_url)
    DBManager.init(db_url, eval(app.config['DB_LOG_FLAG'])) #eval ->안하면 스트링
    DBManager.init_db()
### 뷰 처리 ###
    from service.controller import login
    from service.app_blueprint import blueprint
    app.register_blueprint(blueprint)
### 글로벌 오류 등록(404, 500) ###
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, server_error)
    
    return app
##################################################################
# config
def print_config(config):
    print("*"*100)
    print( config )
#     for key in config:
#         print("%s=%s"%(key,config['key']))
    for key, value in config:
        print("%s=%s" % (key, value) )
    print("*"*100)
##################################################################            
