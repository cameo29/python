'''
Created on 2017. 11. 7.
Flask 
/        홈페이지 (로그인 링크)
-------------------------------------------
/login   로그인폼(get), 로그인처리(post)
/main    메인페이지(특정정보출력:DB에서 가져오기)
/search  메인페이지 위에 검색창의 검색 AJAX통신 JSON응답
-------------------------------------------
/newsRegi 글등록(제목, 내용, 첨부파일)
/news     뉴스리스트
/new/<id> 특정글
-------------------------------------------
'''
# 모듈 가져오기(interpreter flask로 설정되있어야함)
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pymysql as my
# 플라스크 객체 생성
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # post로 전달된 데이터 받기
        uid = request.form['uid']
        upw = request.form['upw']
        if loginDataValid(uid, upw):
            if loginDBProc(uid, upw):
                # 쿠키저장
                # 세션저장
                session["uid"] = uid
                # 페이지 이동 /main
                return redirect(url_for("main"))
#                 return 'success'
            else:
                return '<script>alert("회원정보가 일치하지 않습니다.");history.back();</script>'

        else:
            return '<script>alert("정확한 정보 입력하세요.");history.back();</script>'
        
    else: 
        return render_template("login.html")

@app.route("/main")
def main():   
    data = baseballData()
    return render_template("main.html", data=data)

@app.route("/logout")
def logout():
    # 세션제거
    session.pop('uid', None)
    return redirect(url_for("home"))

@app.route("/search", methods=['POST'])
def search():
    # 파라미터 획득
    keyword = request.form['keyword']
    # 쿼리
    rows = getSearchBaseball(keyword)
    print(rows)
    # 결과반환
    return jsonify(rows[0])

@app.route("/upload", methods=["GET","POST"])
def upload():
    if request.method == "POST":
        # input tag name="img_file" 파일 객체 획득
        f = request.files['img_file']
        f.save('C:\\Users\\edu\\eclipse-workspace\\WebBasic\\uploads\\'+ f.filename)
        return "file upload complete"
    else:
        return render_template("upload.html")

@app.route("/newsRegi", methods=["GET","POST"])
def newsRegi():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        auth = request.form['auth']
        f = request.files['img_file']
        f.save('C:\\Users\\edu\\eclipse-workspace\\WebBasic\\uploads\\'+ f.filename)

        #insert
        conn = my.connect(
             host = "localhost"
            ,user = "root"
            ,password = "1234"
            ,db = "python"
            ,charset = "utf8"
        )
        cursor = conn.cursor(my.cursors.DictCursor)
        with conn.cursor() as cursor:
            sql = "INSERT INTO `bbs` (`title`, `auth`,`content`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (title, auth, content))
            conn.commit()
    
        return "file upload complete"
    else:
        return render_template("newsRegi.html")

# 로그인 입력값 체크    
def loginDataValid(uid, upw):
    return uid and upw
# 로그인 디비 처리
def loginDBProc(uid, upw):
    conn = my.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        db = "python",
        charset = 'utf8'
    )
    cursor = conn.cursor(my.cursors.DictCursor)
    sql = "SELECT * FROM users WHERE uid=%s AND upw=%s"
    cursor.execute(sql, (uid, upw))
    rows = cursor.fetchall()
    conn.close()
    return rows

def baseballData():
    conn = my.connect(
         host = "localhost"
        ,user = "root"
        ,password = "1234"
        ,db = "python"
        ,charset = "utf8"
        )
    cursor = conn.cursor(my.cursors.DictCursor)
    sql = "SELECT * FROM baseball"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

def getSearchBaseball(keyword):
    print(keyword)
    conn = my.connect(
         host = "localhost"
        ,user = "root"
        ,password = "1234"
        ,db = "python"
        ,charset = "utf8"
        )
    cursor = conn.cursor(my.cursors.DictCursor)
    sql = "SELECT * FROM baseball where name = %s"
    cursor.execute(sql, keyword)
    rows = cursor.fetchall()
    conn.close()
    return rows

# 보안키    
app.secret_key = 'abcdefg'

# 서버가동
if __name__ == "__main__":
    app.run(debug=True)
else:
    print("본 모듈은 단독으로 구동될때 정상 작동합니다.")