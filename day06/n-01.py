# 데이터 분석 시각화, 라이브러리 실습 (도구 사용법)

# 데이터 분석 : 단순히 데이터를 기록하고 읽는 수준이 아닌, 데이터를 체계적으로 수집, 정리하여 숨겨진 패턴과
#               상관관계를 발견하여 유의미한 통찰을 도출하는 과정

# 데이터 분석 과정 첫 번째 : 수집(어떻게 데이터를 수집하고 전처리 할 것인지)

# 인공지능의 등장 이후로 단순 데이터 분석을 한다기보단, [데이터 분석 엔지니어링 + 프롬프트 엔지니어링]


''' =============================================================================================== '''
# 1. numpy 설치 -> pip install numpy
# 2. numpy 불러오기 -> import numpy as np
import numpy as np
print(np.__version__) # 2.5.4

# 3. 넘파이 학습하는 이유 : 1) 데이터 분석(수치계산) / 2) ML/DL 라이브러리들이 사용



'''==================================================================================================='''

# 1. 배열 생성
x = np.array( [1,2,3,4] ) # 1차원 배열
print(x) # [1 2 3 4]

y = np.array([[1, 2, 3], [4, 5, 6 ]]) # 2차원 배열
print(y) 
# [[1 2 3]
#  [4 5 6]]

# 동적(자동으로 타입 정해주는) 타입은 느림, 넘파이는 정적 타입
x = np.array( [1, True, "안녕"] ) 
print(x) # ['1' 'True' '안녕'] -> 타입이 섞이면 문자열로 통일시켜버림

# 2. 0으로 배열 초기화 : np.zeros((행개수, 열개수))

x = np.zeros((2,3))
print(x)
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 3. 1로 채워진 배열로 초기화
x = np.ones((2, 3))
print(x)
# [[1. 1. 1.]
#  [1. 1. 1.]]

# 4. arange( 시작인덱스, 끝인덱스, 단계)
x = np.arange(0,10,2)
print(x) # [0 2 4 6 8]

# 5. linspace( 시작값, 끝값, 사이 범위 )
x = np.linspace(0,1,5)
print(x) # [0.   0.25 0.5  0.75 1.  ]

# ※ 넘파이는 리스트 또는 튜플 타입의 자료들을 넘파이 타입으로 변환할 수 있다.

# 6. 배열 길이 확인
x = np.array([[1,2,3],[4,5,6]])
print(x.shape) # (2, 3) -> 2행 3열

# 7. 배열 타입 확인
x = np.array( [1.0, 2.0, 3.0] )
print(x.dtype) # float64

# 8. 배열 차원 개수 확인
x = np.array( [ [1,2,3],[4,5,6]] )
print( x.size ) # 요소/자료 개수 -> 6
print( x.ndim ) # 차원 개수 -> 2

# 9. 배열의 데이터 타입, np.array( 리스트/튜플, dtype = np.타입명 )
# np.타입명(비트수) 32bit --> 4byte
# np.bool_ : 언더바 주의( 파이썬 bool vs 넘파이 bool_)
# np.bytes : 영문 또는 일부 특수문자(아스키코드) 1바이트
x = np.array( [1,2,3], dtype=np.int32)
print(x.dtype) # int32
x = np.array( [1.0, 2.0, 3.0], dtype=np.float32)
print(x.dtype) # float32
x = np.array( [True, False, True], dtype=np.bool_)
print(x.dtype) # bool
x = np.array(["apple","banana","cherry"], dtype=np.bytes_)
print(x)
print(x.dtype) # |S10


# 10. 타입 변환
x = np.array([1.5, 2.5, 3.5], dtype=np.float32)
y = x.astype(np.int32)
print(y) # [1 2 3]

# ※ 타입 지정한 이유 : 
# 1) 메모리 효율성/속도 
# 2) 텐서플로우/파이토치 라이브러리 속도 향상