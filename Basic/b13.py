'''
Created on 2017. 11. 6.

@author: edu
python class
'''
# 파이썬 클래스
# 파이썬에서 자기 자신 객체를 지칭하는 키워드: self
class MyClass:
    # 변수
    name = 'jaein'
    ''' 
      생성자 / 모든 함수는 무조건 첫번째 인자가 self이다
    '''
    def __init__(self, paramName):
        self.name = paramName        
    # 함수
    def getName(self):
        return self.name

obj = MyClass('KIM')
print(obj.name)
print(obj.getName())
    
print("*"  * 100)