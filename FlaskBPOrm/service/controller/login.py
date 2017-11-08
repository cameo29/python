'''
Created on 2017. 11. 8.
뷰, 컨트롤러 파트
로그인 관련 라우팅, 디비 쿼리 사용, 응답
'''
# import
from flask import render_template, request
from service.app_blueprint import blueprint
from service.app_database import dao
from service.model.user import User
# routing
@blueprint.route('/')
def index():
    # 회원가입
    #insert
#     user = User('nia','nia@k.com','1234')
#     dao.add(user)
#     dao.commit()
    # 회원정보수정
    # select
#     user = dao.query(User).filter_by(username='nia', email='nia@k.com').first()
#     print(user)
    # update
#     user.email = 's@s.com'
#     dao.commit()
    # delete
#     user = dao.query(User).filter_by(username='nia').first()
#     dao.delete(user)
#     dao.commit()
    return render_template('home.html')
# 종료처리
@blueprint.teardown_request
def close_db_session(exception=None):
    try:
        print('session 종료 ')
        dao.remove()
    except Exception as e:
        print(e)
