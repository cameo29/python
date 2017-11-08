'''
Created on 2017. 11. 6.

@author: edu
python while, for
'''
# 파이썬 for(지정된 횟수, 루프의 횟수를 알고 있을때)
a = ['A','B','C']
# a에서 하나씩 꺼내서 str에 담는다
for str in a:
    print(str)
# 튜플 - 타입맞춰서 써줌
a = [(1,2),(3,4),(5,6)]
for (i,j) in a:
    print(i,j)
print("*"  * 10)
# 연속된 수로 리스트를 생서
a = range(1, 11)
print(a)
for b in a:
    print(b)
# 구구단 3단에서 8단
a = range(3,9)
b = range(1,10)
for str in a:
    for str2 in b:
        print("%2d x %2d = %2d" % (str, str2, str*str2)) 

# 축약
print([i*j for i in range(3,9) for j in range(1,10)])
