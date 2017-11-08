'''
Created on 2017. 11. 6.

@author: edu
python class 상속
'''
# 파이썬 클래스
# 파이썬에서 자기 자신 객체를 지칭하는 키워드: self
class MyClass:
    # 변수
    name = 'jaein'
    ''' 생성자 / 모든 함수는 무조건 첫번째 인자가 self이다'''
    def __init__(self, paramName):
        self.name = paramName        
        print("parent constructor call", self.name)
    # 함수
    def getName(self):
        return self.name

#자식 클래스(부모클래스)
class ChildClass(MyClass):
    def __init__(self, paramName):
        self.name = paramName
        print("child constructor call", self.name)
    # 재정의
    def getName(self):
        return self.name+"님 이름"

obj1 = MyClass("hi")
obj = ChildClass("KIM")
print(obj1.name, obj1.getName())
print(obj.name,obj.getName())