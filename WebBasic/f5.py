'''
Created on 2017. 11. 7.
Flask 라우팅 응용 => 동적 파라미터
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask
# 플라스크 객체 생성
app = Flask(__name__)

# 동적파라미터 데이터는 함수의 인자값으로 전달
@app.route('/userInfo/<uid>')
def userInfo(uid):
    return 'hello userinfo : userid is %s' % uid

# 동적 파라미터에 타입을 지정 (int, float, path)
@app.route('/login/<int:sid>')
def login(sid):
    return "user sid is %d" % sid

# 동적 파라미터 구성
# 기본 url /math
# 동적 파라미터 1: x1 (int), 2: y1 (float), 3: type(json)
@app.route('/math/<int:x1>/<float:y1>/<type>')
def math(x1, y1, type):
    return "%d %2.2f %s" % (x1, y1, type)

# 서버가동
if __name__ == "__main__":
    # 서버가동
    app.run()
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")