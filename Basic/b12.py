'''
Created on 2017. 11. 6.

@author: edu
python
'''
# 파이썬 함수
# 함수 기본형
def sum(a, b):
    return a+b
print(sum(1,2))
print("*"  * 100)
# 가변인자
def sum2(*params):
    #인자 오는대로 다 더해서 반환
    a = 0
    for p in params:
        a = a + p
    return a
print(sum2(1,2,3,4,5,6,7,8,9))
# 가변인자인데 결과가 2개, 하나는 모두 더해서, 하나는 모두 곱해서 반환
def sum3(*params):
    a = 0
    b = 1
    for p in params:
        a = a + p
        b = b * p
    return (a,b)
print(sum3(1,2,3,4,5))
# 함수 인자 초기값 부여
def person(name, age, height=100):
    print(name, age, height)

person("k",25,180)
person("h",30)

    