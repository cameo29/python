'''
Created on 2017. 11. 6.

@author: edu
python
'''
# 파이썬 변수: 문자형
print("*"  * 100)
a = '가나다'
b = "ABC"
c = ''' ff '''
d = """ dasf """
print(a,b,c,d)
# ''' """ 사용이유: 가독성, 주석용, 구조유지
'''
가나다 ABC  ff   dasf 
'''
print("*"  * 100)
a = "12345'6789"
b = '123"45'
c = "111234\'4"
d = "1234\"44"
print(a,b,c,d)
print("*"  * 100)
# 문자열 더하기
a = "123"
b = "567"
print(a+b)
print("*"  * 100)
# 문자열 반복
print("*"  * 100)
# 문자열 인덱싱 (0~>..)
a = "0123456789"
# 앞에서부터 세는 인덱싱(0~)
print(a[3], a[0], a[9])
# 뒤에서부터 세는 인덱싱 (-1~)
print(a[-3], a[-1], a[-9])
# 슬라이싱 => [인덱스:인덱스]
print(a[:]) # 전부다
print(a[3:]) # 3부터 끝까지
print(a[:3]) # 3까지
#678 출력
print(a[6:9])
# 678 역방향
print(a[6:-1])
#################################################
# 문자열 immutable -> 문자열 자체는 변경 불가
# 문자열을 변경하고 싶으면 슬라이싱후 합쳐서 생성해야함
print("*"  * 100)
# 포맷팅 % or .format()
print("%s %d + %d = %d" % ( '더하기', 1, 2, (1+2) ) )
print("%s %s + %s = %s" % ( '더하기', 1, 2, (1+2) ) )
print("{0} {1} + {2} = {3}" .format( '더하기', 1, 2, (1+2) ) )
print("{0} {a1} + {a2} = {a3}" .format( '더하기', a1=1, a2=2, a3=(1+2) ) )
#################################################
# 정렬 및 공백(자리수 맞춤)
print("*" * 100)
a = "%20s" % "12345"
print(a)
a = "%-20s" % "12345"
print(a)
a = "%0.4f" % 3.1434832727
print(a)
a = "%10.4f" % 3.1434832727
print(a)
a = "%-10.4f" % 3.1434832727
print(a)
#################################################
# 문자열 개수
# 문자끼리 비교, 숫자끼리 비교
a = "0123456789"
print("*" * 100)
print(a)
print("4라는 문자가 몇개?")
print(a.count("4"))
print("특정문자의 인덱스 찾기 =>", a.find("4"))
# 조인
c = ","
print(c.join(a))
# 공백 지우기
a = "  a  "
print("["+a.lstrip()+"]")
print("["+a.rstrip()+"]")
print("["+a.strip()+"]")
# 대소문자 처리
a = "asdjfklasdjfASDFF"
print(a, a.upper(), a.lower())
# 대체
print(a.replace("asd", "=="))
# 나누기
a = "123456789"
b = ","
c = b.join(a)
print(c)
print(c.split(b)) # 결과 : 리스트
# 형변환
a = 10
print(str(a))
# 치환식
a = "가나다{0}1234".format("a")
print(a)
a = "가나다{0:<10}1234".format("a")
print(a)
a = "가나다{0:>10}1234".format("a")
print(a)
a = "가나다{0:^10}1234".format("a")
print(a)
a = "가나다{0:*^10}1234".format("a")
print(a)
a = "가나다{0:*<10}1234".format("a")
print(a)



