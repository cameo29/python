'''
Created on 2017. 11. 6.

@author: edu
python
'''
# 파이썬 자료형: 리스트, (list), 배열을 연상, 순서 존재, 0부터 시작, 인덱스 있음, 중복 허용
#            리스트 구성요소(원소)의 타입은 동일해야 하는가? 관계없음, 크기도 자유롭게 조정가능
print("*"  * 100)
# 원소 구분은 , 전체 외곽은 []
odd = [1, 3, 5, 7, 9]
print(odd)
word = ["dog",'cat','bird']
print(word)
mix = [2,4,"person"]
# 타입이 섞여도 상관없음
print(mix)
# 차원이 섞여도 상관없음
matrix = [1,2,3,[5,6]]
print(matrix)
# select
print(odd[0], mix[2], matrix[3], matrix[3][0])
print(matrix[3][-1])
# slicing
print(word[0:2])
# 더하기
print(odd + word)
# 반복
print(odd * 10)
# 수정
print(odd)
# 원본수정(리스트는 가능 문자열은 안돼)
odd[0] = 100
print(odd)
# 슬라이싱 구간에 리스트로 덮기
odd[0:2] = word
print(odd)
print("*" * 10)
# 리스트 삭제
print(mix)
del mix[2]
print(mix)
print(word)
del word[0:2]
print(word)
# 추가
list = [1,2,3,4]
list.append(5)
print(list)
list.append([6,7]) # 1,2,3,4,5,6,7 하려면 그냥 더하기~
print(list)
list.remove([6,7]) # 값으로 제거
print(list)
# 정렬
list = [2,5,1,3,6,3,7]
list.sort()
print(list)
list.reverse()
print(list)
# 꺼내기(제거후 반환)
print(list.pop())
print(list)


