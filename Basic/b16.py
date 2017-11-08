'''
Created on 2017. 11. 6.

@author: edu
python
'''
# 파이썬 내장함수(파일, 콘솔입력)
# 파일: 내장 함수로 바로 사용 가능
f = open("z.txt",'w')
f.close()
print("*"  * 100)
# 파일쓰기
f = open("z.txt",'w')
for i in range(1, 10):
    data = "%d번째 라인\n" % i
    f.write(data)
f.close()
# 파일읽기
f = open("z.txt",'r')
while True:
    data = f.readline()
    print(data)
    if not data:
        break
f.close()
# 자동 닫기
with open("z.txt",'r') as t:
    while True:
        data = t.readline()
        print(data)
        if not data:
            break
