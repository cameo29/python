'''
Created on 2017. 11. 6.
Database 접속 및 해제
mariaDB 사용
pymysql 모듈 사용
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
    )
# 데이터 가져오기
# 커서획득
cursor = conn.cursor()
# 쿼리수행
sql = "select * from users order by regdate desc;"
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)
# 이름만 출력
# print(rows[0][3],rows[1][3])
for row in rows:
    print(row[3])
# 디비연결종료
conn.close()