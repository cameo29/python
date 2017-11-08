'''
Created on 2017. 11. 6.

@author: edu
python boolen
'''
# 파이썬 블린 => True, False(0, 리스트, 튜플, 딕셔너리 => 데이터가 없다 )
print("*"  * 100)
a = [1,2,3,4]
while a:
    print(a.pop())
print("loop end", a)
#참조 카운트 : as 별칭, 수치도 객체, 같은 값을 받으면 가르키고 있는 객체가 동일
import sys as s
a = 1
print(a, type(a), s.getrefcount(1))
b = 1
print(a, type(b), s.getrefcount(1))
print(a is b) #조건식
del a
print(s.getrefcount(1))
del b
print(s.getrefcount(1))