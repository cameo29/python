'''
Created on 2017. 11. 6.

@author: edu
python
'''
# 파이썬 예외처리 : 프로그램은 중단되면 안된다^^
print("*"  * 100)
try:
    print(1)
    print(2)
    28302/0
    print(3)
    print(4)
except ZeroDivisionError as e:
    print(e)
    