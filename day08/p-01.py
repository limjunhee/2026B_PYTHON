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

df = pd.DataFrame(
    data_np,
    columns= ['name', 'age', 'city'],
    index=[ 'A', 'B', 'C']
)
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

df.info() # 타입, 컬럼이름, 결측치 등 데이터프레임의 전체적인 정보를 출력함( 함수 자체가 출력 기능이 있어 print 필요 없다.)
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


# ========================================================================================================================================================================

# 6) 인덱싱 = df.iloc[행 인덱스, 열 인덱스]

df = pd.DataFrame(
    data_np,
    columns= ['name', 'age', 'city'],
    index=[ 'A', 'B', 'C']
)
print(df)
print( df.iloc[1] )
'''
[df.iloc[1] 출력 결과]

name      bee
age        30
city    busan
Name: B, dtype: str
'''

print( df.iloc[1, 2] ) # busan 출력 -> 1행의 2열

print( df.loc['B'] ) # 1행(B행) 출력 -> index 속성으로 A,B,C 를 넣었기에 가능

print( df.loc['B', 'city'] ) # B행의 city 열을 출력 -> busan

# 칼럼, 인덱스에 특정 이름을 넣으면 그 이름으로도 인덱싱을 할 수 있게 지원한다.


# ========================================================================================================================================================================

# 7) 슬라이싱 , [시작 인덱스 : 끝 인덱스]
df = pd.DataFrame(
    data_np,
    columns= ['name', 'age', 'city'],
    index=[ 'A', 'B', 'C']
)

print(df.iloc[0:2, 0:1]) # 0행, 1행의 name만 가져오기 ( 기본 파이썬과 똑같이 끝 인덱스를 제외 -> 끝 인덱스 -1까지만 가져온다. )
'''
[출력 결과]

  name
A  ant
B  bee
'''

print( df.loc[ 'A':'C' , 'name':'age']) # 이름으로 인덱싱 -> 이땐 끝 인덱스-1 까지 슬라이싱이 아니다. 끝 칼럼을 포함한다.
'''
[출력 결과]

  name age
A  ant  25
B  bee  30
C  cat  35
'''


# ========================================================================================================================================================================

# 8) 열 추가, df[새로운 열] = 새로운 값
df = pd.DataFrame(
    data_np,
    columns= ['name', 'age', 'city'],
    index=[ 'A', 'B', 'C']
)

df['score'] = [100, 80, 95] # 행 개수에 안맞추면 오류뜸
print(df)
'''
[열 추가 후 출력 결과]

  name age     city  score
A  ant  25    seoul    100
B  bee  30    busan     80
C  cat  35  incheon     95

'''

# ========================================================================================================================================================================

# 9) 값 수정, df[수정할 열] = 새로운 값
df['age'] = [31, 40, 24] # 행 개수에 안맞추면 오류뜸
print(df)
'''
[age 수정 후 결과]

  name  age     city  score
A  ant   31    seoul    100
B  bee   40    busan     80
C  cat   24  incheon     95
'''


df.loc['B','age'] = 70 # B 행의 age 열 값을 수정하라는 뜻
print(df)
'''
[B행의 age 열 값 수정 후 결과]

  name  age     city  score
A  ant   31    seoul    100
B  bee   70    busan     80
C  cat   24  incheon     95
'''


df.loc[0,0] = 'apple' 
print(df)
'''
[0 이름을 가진 행과 열 추가]

  name   age     city  score      0
A  ant  31.0    seoul  100.0    NaN
B  bee  70.0    busan   80.0    NaN
C  cat  24.0  incheon   95.0    NaN
0  NaN   NaN      NaN    NaN  apple
'''


# ========================================================================================================================================================================

# 10) 여러 개 수정하기
df.loc[['A','B'], 'score'] = [50, 60] # A행의 score를 50으로, B행의 score를 60으로 수정하라
print(df)

'''
[값 2개 수정 후 결과]

  name   age     city  score      0
A  ant  31.0    seoul   50.0    NaN
B  bee  70.0    busan   60.0    NaN
C  cat  24.0  incheon   95.0    NaN
0  NaN   NaN      NaN    NaN  apple
'''

# ========================================================================================================================================================================

# 11) 필터링(조건) 입력 
print(df['score'] > 70) # 50, 60, 95, NaN 총 4개와 조건 비교 -> score 요소값들의 T/F 리스트로 출력 
'''
[출력결과]

A    False
B    False
C     True
0    False
Name: score, dtype: bool
'''


print(df[ df['score'] >= 70 ] ) # 원본에서 조건이 True인 "행"을 출력 -> 조건이 참인 부분을 가진 행 전체를 추출하여 출력해준다.
# ※ 넘파이 인덱싱과 비슷하게 T/F 리스트가 아닌 조건이 True인 값들을 보려면 대괄호 안에 대괄호를 한 번 더 넣는 형식으로 작성해야 한다(헷갈림)
'''
[출력결과]

  name   age     city  score    0
C  cat  24.0  incheon   95.0  NaN
'''

cont = df['age'] >= 40
print( df[ (df['score'] > 70) & cont ])
print( df[ (df['score'] > 70) | cont ])

# 필터링 이용하여 새로운 열 만들기 (원본을 변경하지 않음)
df['passed'] = False
df.loc[ df['score'] > 70, 'passed'] = True # 'passed'라는 새로운 열을 맨 뒤에 만들고, score가 70 초과인 행은 True로 변경하라
print(df)
'''
[출력 결과]

  name   age     city  score      0  passed
A  ant  31.0    seoul   50.0    NaN   False
B  bee  70.0    busan   60.0    NaN   False
C  cat  24.0  incheon   95.0    NaN    True
0  NaN   NaN      NaN    NaN  apple   False
'''


# ========================================================================================================================================================================

# 12) 칼럼명 변경. df = df.rename( columns = { 기존열이름:새로운열이름 } )
df = df.rename( columns= { 'city' : '도시' , 'age' : '나이' } )
df.info()
'''
<class 'pandas.DataFrame'>
Index: 4 entries, A to 0
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   name    3 non-null      str    
 1   나이      3 non-null      float64
 2   도시      3 non-null      str    
 3   score   3 non-null      float64
 4   0       1 non-null      str    
 5   passed  4 non-null      bool   
dtypes: bool(1), float64(2), str(3)
memory usage: 368.0+ bytes
'''


# ========================================================================================================================================================================

# 13) 집계, df.describe()
print(df.describe()) # 정수/실수 자료값을 가진 컬럼의 전체적인 집계를 알려줌

print(df['나이'].sum()) # 나이 컬럼의 총합

print( df['passed'].value_counts()) # 자료 빈도 수 -> passed 열의 True가 1개, False가 3개임을 알려줌


# ========================================================================================================================================================================

# 14) 합치기/병합
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Score': [90, 80, 85]})
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Score': [75, 95, 88]})

# 세로 연결 pd.concat( [df1, df2], axis = 0) 
# ※ axis의 0은 기본값
new_df = pd.concat( [df1, df2] , axis = 0, ignore_index = True)
print(new_df)
'''

   ID  Score
0   1     90
1   2     80
2   3     85
3   4     75
4   5     95
5   6     88

'''



new_df = pd.concat([df1,df2], axis=1, ignore_index=True)
print(new_df)
'''

   0   1  2   3
0  1  90  4  75
1  2  80  5  95
2  3  85  6  88

'''



# 속성이 다른 데이터프레임끼리의 병합 -> 교집합(공통 컬럼)
# pd.merge(df1, df2, on = '공통컬럼명', how=방향)
df_info = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})
df_score = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})

new_df = pd.merge(df_info, df_score, on = 'ID', how = 'inner')
print(new_df)

'''
[병합 결과]

   ID Name  Score
0   2  Bee     88
1   3  Cat     92
'''

new_df = pd.merge(df_info, df_score, on = 'ID', how = 'outer')
print(new_df)
'''
[병합 결과]
   ID Name  Score
0   1  Ant    NaN
1   2  Bee   88.0
2   3  Cat   92.0
3   4  NaN   85.0
''' # NaN : 정의가 없는 자료


# ========================================================================================================================================================================

# 15) 정렬 - df.sort
df = pd.DataFrame({
  'name': ['Ant', 'Bee', 'Cat', 'Dog'],
  'age': [27, 27, 22, 32],
  'score': [88, 95, 85, 90]
})

# df.sort_values( by = '컬럼명' , ascending=True 오름차순 / False 내림차순)
new_df = df.sort_values( by = 'age' , ascending = False )
print(new_df)
'''
  name  age  score
3  Dog   32     90
0  Ant   27     88
1  Bee   27     95
2  Cat   22     85
'''

# 다중 정렬은 [] 리스트 사용, *age 기준으로 1차 정렬 후 동이랗ㄴ age끼리 score기준으로 2차 정렬
new_df = df.sort_values( by = ['age', 'score'] , ascending = [True, False] )
print(new_df)
'''
  name  age  score
2  Cat   22     85
1  Bee   27     95
0  Ant   27     88
3  Dog   32     90
'''

# 컬럼명도 정렬 가능, axis = 0행/1열
new_df = df.sort_index( axis=1, ascending = True )
print(new_df)
'''
   age name  score
0   27  Ant     88
1   27  Bee     95
2   22  Cat     85
3   32  Dog     90
'''

# ========================================================================================================================================================================
