'''
Created on 2017. 11. 7.
Flask ROUTE
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask
# 플라스크 객체 생성
app = Flask(__name__)

# 전체 기획이 완료되면 라우팅을 배치하여 각 요청을 처리할 함수들을 정의해둠
# route()의 데코레이터 함수와 URL을 연결한다.
@app.route('/')
def index():
    print("index() call")
    return 'index page'

@app.route('/hi')
def hi():
    return 'hi page';

# 서버가동
if __name__ == "__main__":
    # 직접 python f2.py 구동
    # 서버가동
    app.run()
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")