'''
Created on 2017. 11. 6.
Database 접속 및 해제
mariaDB 사용
pymysql 모듈 사용
dictionary로 데이터 가져오기
'''
# import 컨벤션(이름이 길어서 별칭사용)
# 예... import pandas as pd
import pymysql as my

# 디비오픈
conn = my.connect(
    host='localhost',
    user='root',
    password='1234',
    db='python',
    charset='utf8'
    # 커서타입 옵션
    #, cursorclass = pymysql.cursors.DictCurdor 
    )
# 데이터 가져오기
# 딕셔너리 커서획득
cursor = conn.cursor(my.cursors.DictCursor)
# 로그인쿼리수행
id = input('id입력: ');
pwd = input('pwd입력: ');
# 파라미터는 %s로 받고, 문자열을 의미하는 것은 아님
sql = "SELECT * FROM USERS WHERE uid=%s and upw=%s;"
cursor.execute(sql, (id, pwd))
rows = cursor.fetchall()
for row in rows:
    print(row['uid'], row['name'])
if rows:
    print('로그인')
else:
    print('없음')

# 디비연결종료
conn.close()