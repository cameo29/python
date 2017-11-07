'''
Created on 2017. 11. 7.
Flask 
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask
# 플라스크 객체 생성
app = Flask(__name__)
# 뒤에 슬래시 붙이면 자동으로 슬래시 붙여줌
# /pro -> /pro/ 경로로 변경됨
@app.route('/pro/')
def pro():
    return "pro page"

# /home => ok , /home/ => 404 에러
@app.route('/home')
def home():
    return "home page"

# 얘는 예외 ~ / 붙이든 안붙이든 404 에러 안남
@app.route('/')
def home1():
    return "page"

# 서버가동
if __name__ == "__main__":
    # 직접 python f2.py 구동
    # 서버가동
    app.run()
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")