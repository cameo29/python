'''
Created on 2017. 11. 6.

@author: edu
python dictionary
'''
# 파이썬 자료형 : 딕셔너리 => 키:값 { } , 키는 고유, 키는 중복되면 안돼, 값은 관계없음, 순서없음
print("*"  * 100)
dic = {"name":"jaein", "age":10}
print(dic)
print(dic["name"],dic["age"])
# 추가
dic[1] = "hi"
print(dic)
# 키의 타입은 반드시 문자열이 아니다
# 삭제
del dic[1]
print(dic)
# 딕셔너리 함수, 리스트형태로 보여줌
print(dic.keys())
print(dic.values())
# 초기화
dic.clear()
print(dic)
dic = {"name":"kim", "age":10}
print("키조사 조건문=>", "name" in dic)
