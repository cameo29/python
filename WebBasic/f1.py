'''
Created on 2017. 11. 7.
Flask 기본구동 확인
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask
# 플라스크 객체 생성
# 모듈로 구동할때와 직접 구동할때 설정되는 이름이 다름: __name__
# __name__이 직접 구동될때의 이름 __main__ 일 경우에만 서버 정상 가동
app = Flask(__name__)

# 라우팅
# url 요청할 때 url을 어떤 함수가 처리할지 매칭
@app.route("/")
def home():
    return "hello flask"

# 서버가동
if __name__ == "__main__":
    # 직접 python f1.py 구동
    # 서버가동
    app.run()
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")