import numpy as np

# 1차원 배열 통계 함수
x = np.array( [1,2,3,4,5] )
print( np.min(x), np.max(x) ) # 최솟값, 최댓값 출력(요소값) -> 1, 5
print( np.argmin( x ), np.argmax( x ) ) # 최솟값, 최댓값이 있는 인덱스 출력 -> 0, 4
print( np.sum(x), np.mean(x), np.median(x)) # 합계, 평균, 중앙값 출력 -> 15, 3.0, 3.0
                                            # 평균, 중앙값은 구하기 위해 나눗셈 해야 하므로 실수형으로 나오는듯?
print( np.var(x) ) # 분산: 평균으로부터 요소 값들이 떨어진 정도(간격) -> 2.0
print( np.std(x) ) # 표준편차(분산의 양의 제곱근 사용하여 데이터 단위 맞춘 값) -> 1.4142135623730951
print( np.sqrt(x) ) # 양의 제곱근(루트) -> [1.         1.41421356 1.73205081 2.         2.23606798]

# 2차원 배열 통계 함수
# np.통계함수(2차원배열, axis = [생략시1차원평탄화, 0 열 기준, 1 행 기준] )
y = np.array( [[1,2,3], [4,5,6]] )
print( np.min(x), np.max(y) ) # 1 6
print( np.min(y, axis=0) ) # axis = 0 : 열 마다 최솟값 구함 # [1 2 3]
print( np.min(y, axis=1) ) # axis = 1 : 행 마다 최솟값 구함 # [1 4]
print( np.argmin(y), np.argmax(y)) # 최솟값, 최댓값이 있는 인덱스 위치 출력 -> 0 5
print( np.sum( y, axis = 0), np.mean( y, axis=0), np.median( y, axis=1)) # [5 7 9] / [2.5 3.5 4.5] / [2. 5.]
print( np.var(x), np.std(x), np.sqrt(x)) # 2.0 / 1.4142135623730951 / [1.         1.41421356 1.73205081 2.         2.23606798]
