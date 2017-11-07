'''
Created on 2017. 11. 7.
Flask 정적위치: css, js, image 는 정적 위치에 위치하여 html에서 인식하여 사용됨
통산 프로젝트내에 폴더 이하 ~
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask, url_for
from fileinput import filename
# 플라스크 객체 생성
app = Flask(__name__)

with app.test_request_context():
    print(url_for('static', filename='layout.css'))

# 서버가동
if __name__ == "__main__":
    # 서버가동
    app.run()
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")