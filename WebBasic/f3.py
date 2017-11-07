'''
Created on 2017. 11. 7.
Flask : 디버깅모드 구동하기 => 개발할때 사용
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask
# 플라스크 객체 생성
app = Flask(__name__)

@app.route("/")
def home():
    return "home page 한글"

# 서버가동
if __name__ == "__main__":
    # 직접 python f2.py 구동
    # 서버가동 디버깅모드(웹화면에 나옴)
    # app.run(debug = True)
    # or
    app.debug = True
    app.run()
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")