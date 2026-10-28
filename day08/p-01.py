import pandas as pd

print(pd.__version__)

# 1) 데이터프레임 : 2차원 표 , pd.DataFrame(리스트, columns = "열이름", "열이름", ....)

data_list = [ [ 'ant' , 25 , 'seoul'] ,
              ['bee' , 30 , 'busan'] ,
              ['cat' , 35 , 'incheon'] ] # 2차원 리스트

x = pd.DataFrame(data_list)
print(x) # 표 모양으로 출력됨

'''
[x 출력 결과]

     0   1        2
0  ant  25    seoul
1  bee  30    busan
2  cat  35  incheon
'''

x = pd.DataFrame( data_list, columns=['name','age','city'])
print(x)

'''
[x 출력 결과]

  name  age     city
0  ant   25    seoul
1  bee   30    busan
2  cat   35  incheon
'''


# ========================================================================================================================================================================



# 2) 데이터프레임2 , pd.DataFrame( 딕셔너리 ) -> 이때, 열 이름은 키 이름으로 결정됨
data_dict = { 
  'name' : ['ant','bee','cat'] , 
  'age' : [25,30,35] , 
  'city' : ['seoul','busan','incheon'] } # 딕셔너리

x = pd.DataFrame(data_dict)
print(x)



# ========================================================================================================================================================================




# 3) 컬럼 값 추출, df['열이름']
df = pd.DataFrame( data_list, columns=['name','age','city'])

ages = df['age']
print( ages )

'''
[age 출력 결과]

0    25
1    30
2    35
Name: age, dtype: int64
''' # 인덱스(행 번호)와 age열의 요소값들을 출력 

print(type(ages))           # <class 'pandas.Series'> -> Series는 pandas의 1차원 배열(Vector)!
print(type(ages.values))    # <class 'numpy.ndarray'> -> pandas도 넘파이가 내장되어 있다는 증거


# ========================================================================================================================================================================



# 4) 데이터프레임 3 : Numpy 응용 -> pd.DataFrame( 자료, columns = [],, index = [])
import numpy as np
data_np = np.array( data_list ) # Numpy 자료

df = pd.DataFrame( data_np ) # Numpy 자료로 Pandas 데이터프레임 생성
print(df)

'''
[df 출력 결과]

     0   1        2
0  ant  25    seoul
1  bee  30    busan
2  cat  35  incheon
'''

df = pd.DataFrame(
    data_np,
    columns= ['name', 'age', 'city'],
    index=[ 'A', 'B', 'C']
)
print(df)

'''
[df 출력 결과]

  name age     city
A  ant  25    seoul
B  bee  30    busan
C  cat  35  incheon
'''


# ========================================================================================================================================================================



# 5) 주요 속성
print(df.shape) # 행/열 크기 -> (3, 3)
print(df.columns) # 컬럼 목록 -> Index(['name', 'age', 'city'], dtype='str')
print(df.index) # 인덱스 목록 -> Index(['A', 'B', 'C'], dtype='str')
print(df.values) # 값만 추출
'''
[df.values 출력 결과]

[['ant' '25' 'seoul']
 ['bee' '30' 'busan']
 ['cat' '35' 'incheon']]
'''

# 데이터 잘 가져왔는지 확인용으로 사용
print(df.head( 2 )) # 상위 행 n개만 반환(기본값은 5)
print(df.tail( 2 )) # 하위 행 n개만 반환(기본값 5)

df.info() # 타입, 컬럼 등 데이터프레임의 전체적인 정보를 출력함( 함수 자체가 출력 기능이 있어 print 필요 없다.)
'''
[df.info() 결과]

<class 'pandas.DataFrame'>
Index: 3 entries, A to C
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    3 non-null      str  
 1   age     3 non-null      str  
 2   city    3 non-null      str  
dtypes: str(3)
memory usage: 96.0+ bytes
'''