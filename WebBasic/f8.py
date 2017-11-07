'''
Created on 2017. 11. 7.
Flask restful, get, post
/login get 요청 => 로그인 폼
/login post 요청 => 로그인 프로세스  요청(db)
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask, request
# 플라스크 객체 생성
app = Flask(__name__)

# login get, post 지원
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return goPostLogin()
    else: 
        return goGetLogin()

def goGetLogin():
    return "로그인 폼 화면"

def goPostLogin():
    return "로그인 처리 화면"

# 서버가동
if __name__ == "__main__":
    # 직접 python f2.py 구동
    # 서버가동
    app.run()
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")