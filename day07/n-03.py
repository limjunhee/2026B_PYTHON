import numpy as np

# 1) 리스트 병합
x = np.array([[1,2],[3,4]]) # 2차원 리스트
y = np.array([[5,6],[7,8]]) # 2차원 리스트
z = np.vstack([x,y])
print(z)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''

z = np.hstack([x,y])
print(z)
'''
[[1 2 5 6]
 [3 4 7 8]]
 '''

# 2) 병합2 np.concatenate( (배열1, 배열2), axis = [0 or 1] )
z = np.concatenate((x,y), axis=0) # axis = 0 -> 열(세로) 방향
print(z)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''

z = np.concatenate((x,y), axis=1) # axis = 1 -> 행(가로) 방향
print(z)
'''
[[1 2 5 6]
 [3 4 7 8]]
'''

# 3) 정렬
x = np.array([3,1,4,2,5]) # 오름차순으로 정렬(기본값)
print(np.sort(x)) # 1 2 3 4 5
print(np.sort(x)[::-1]) # 5 4 3 2 1
print(x) # 원본 변경 X

x.sort() # 배열.sort()
print(x) # 1 2 3 4 5 -> 원본 자체가 변경, np.sort가 비파괴적 방식 / 원본 자체를 정렬하고 싶다면 np를 빼고 sort()할 것.


# 4) 값 자체를 정렬하지 않고 배열을 정렬 위치순번 반환
scores = np.array([46,36,87,96,66])
print(scores)
z = np.argsort( scores )
print( z ) # 1 0 4 2 3 -> 오름차순을 기준으로, 해당 요소값들이 정렬되는 순서만 알려줌 (실제로 정렬은 안함)
            # 값을 오름차순으로 줄 세우고, 그 순서대로 각 값의 원래 인덱스만 출력하는 것
print(np.sort(scores))

# 5) 필터링/조건식, *for문 사용 안할 수 있음 : 내부적으로(라이브러리) for문 사용됨
x = np.array([10,20,30,40,50])
print(x > 30) # [False False False  True  True]
print(x[x > 30]) # 인덱싱 안에서 조건식 사용하면 True인 값만 추출함 -> [40 50]

y = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
print(y % 2 == 0)
'''
[[False  True False]
 [ True False  True]
 [False  True False]]
'''

print(y[y % 2 == 0]) # 참이면 값을 가져옴(if문) -> [2 4 6 8]


# 6) 삼항 연산자, np.where(조건, 참, 거짓)
print( np.where( x > 30, x , 0 ) ) # [ 0  0  0 40 50]
print( np.where( y % 2 == 0, 1, 0 ) )
'''
[[0 1 0]
 [1 0 1]
 [0 1 0]]
'''

# 7) 다수 조건, & | ~
a = y % 2 == 0 # (짝수 조건을 변수화하는 방식)
print( y[ a & (y % 4 == 0) ] ) # y 요소값이 짝수이면서 4의 배수일 경우 -> 4 8
print( y[ a | (y % 4 == 0) ] ) # y 요소값이 짝수이거나 4의 배수일 경우 -> 2 4 6 8
print( y[ ~a ]) # y 요소값이 짝수가 아닐 경우 -> 1 3 5 7 9

# ※주의 : C/JAVA 에서 &비트(0/1)연산자, numpy에서는 &논리연산자
# 넘파이는 파이썬에서 실행되는 구조이기 때문에 중복에 따른 오버라이딩 제한 존재 -> bool vs bool_
# 넘파이는 and를 쓸 수 없다(파이썬에서 이미 and를 사용하고 있기 때문에)


# 인덱싱 결과를 T/F 리스트로 보고 싶다면 조건식만,
# 인덱싱 한 (True만 출력한) 결과를 보고 싶다면 인덱싱 대괄호 안에 조건식을 넣자. 