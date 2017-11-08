'''
Created on 2017. 11. 8.
어플리케이션 컴포넌트를 만들고, 어플내부와 어플간의 공통 패턴을 지원하는 기능: blueprint 정의
flask 에서 지원
'''
from flask import Blueprint

blueprint = Blueprint('service'
                      , __name__
                      , template_folder='templates'
                      , static_folder='static')

print(blueprint)
