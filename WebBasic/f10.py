'''
Created on 2017. 11. 7.
Flask html을 랜더링 하여 처리 => 템플릿엔진 => jinja2(신사)를 사용
render_template : 랜더링 담당
{% %} 문장 블럭
{{ }} 값 출력
{# #} 주석
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask, render_template
# 플라스크 객체 생성
app = Flask(__name__)

# 2개의 라우팅을 하나의 함수에 적용
# uid가 있거나 없거나 라우팅(uid 초기값 none)
# index.html 파일은 templates 밑에 있어야함
@app.route('/main/')
@app.route('/main/<uid>')
def main(uid=None):
    return render_template('index.html', uid=uid)

# 서버가동
if __name__ == "__main__":
    # 서버가동
    app.run(debug=True)
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")