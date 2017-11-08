'''
Created on 2017. 11. 6.

@author: edu
python
'''
# 파이썬 집합: 중복허용하지 않음. 순서존재
print("*"  * 100)
a = set([1,2,3,4,5,6,7,7,8,8,9])
print(a)
a = set("helloworld")
print(a)
print(list(a))
print(tuple(a))
#################################
print("*" * 100)
# 합집합, 교집합, 차집합
a = set([1,2,3,6,8])
b = set([2,4,5,7,8])
# 합집합
print(a.union(b))
# 교집합
print(a.intersection(b))
# 차집합 빼는 방향에 따라 다름
print(a.difference(b), b.difference(a))
#################################
print("*" * 100)
print(a)
a.add(10)
print(a)
a.update([11,12,13])
print(a)
a.remove(3)
print(a)