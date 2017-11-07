'''
Created on 2017. 11. 7.
Flask url을 직접 기록할것인가?
함수를 통해서 구할것인가?
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask, url_for
# 플라스크 객체 생성
app = Flask(__name__)

# /
@app.route("/")
def home():pass
# /login
@app.route("/login")
def login():pass
# /user/<username>
@app.route("/user/<username>")
def user(username):pass
##############################
# url_for('라우트아 연결된 함수명') => 정확한 URL을 획득할 수 있다.
# URL을 사용하는 곳에는 url_for()를 사용하면 추후 변경시에도 유연하게 적용된다. 
with app.test_request_context():
    print(url_for("home"))
    print(url_for("login"))
    print(url_for("user", username="pop"))

# 서버가동
if __name__ == "__main__":
    # 직접 python f2.py 구동
    # 서버가동
    app.run()
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")