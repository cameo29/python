'''
Created on 2017. 11. 6.

@author: edu
python 모듈, 패키지
'''
# 파이썬 모듈, 패키지
print("*"  * 100)

# from 모듈명 import 모듈[xxx.py](함수, 변수, 클래스) as 별칭
# import 모듈(경로인식되면)

#from a.b import mod as m
#print(m.sum(1,2))

# a.b. 에 있는 모든 모듈을 가져다 쓰고 싶다면 ~~~? 
# __init__.py 에 기술 해줘야함 ! 안해주면 오류
from a.b import *
print(mod.sum(1,2))
print(mod2.sum(1,2))
print(mod.sub(1, 2))
print(mod2.sub(1,2))
