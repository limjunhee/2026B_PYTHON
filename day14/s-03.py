# 1) 항 추가하는 함수
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures() # 객체 생성
poly.fit( [[ 2 ]] )         # 특성(2) 규칙
print( poly.transform([[2]])) # [[1. 2. 4.]] -> 기본절편, 원래값, 제곱값
poly.fit( [[ 3 ]] )
print( poly.transform([[3]])) # [[1. 3. 9.]]

# 2) 절편 제외
poly = PolynomialFeatures( include_bias=False )
poly.fit( [[2]] )       # 특성(2) 규칙
print( poly.transform( [[ 2  ]] )) # [[2. 4.]]

# 3) 특성이 2개인 경우
poly = PolynomialFeatures( include_bias=False )
poly.fit([[2,3]])               # 특성 [2, 3] 규칙 (제곱/곱셈)
print( poly.transform( [[2,3]] )) # 2,3 / 4,9 / 6 -> 원래값 / 특성 각각의 제곱값 / 두 특성을 곱한 값

# *) 특성 3개인 경우
poly = PolynomialFeatures( include_bias=False )
poly.fit([[2,3,4]])
print( poly.transform([[2,3,4]])) # 9개
# 수동으로 특성의 제곱항을 만들지 않고 자동으로 PolynomialFeatures를 이용하여 다항 추가


# [2] 다항 회귀 모델
import pandas as pd
df = pd.read_csv('./day14/Fish.csv')

# 1) 특성 및 타깃 구성
x = df[['Length2','Height','Width']] # 특성 3개
y = df['Weight']                     # 타깃 1개

# 2) 훈련용/테스트용 분리 8:2
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state=42 )

# 3) 과소적합 해결/방지 하고자 항 추가 == PolynomialFeatures
poly = PolynomialFeatures( include_bias = False )
poly.fit(x_train) # 학습할 특성들을 규칙(제곱/곱셈) 찾기
x_train_poly = poly.transform(x_train)
x_test_poly = poly.transform(x_test)
print( x_train.shape ) # (127, 3) 127행 3열(특성)
print( x_train_poly.shape) # (127, 9) 127행 9열 (특성 -> 항 추가됨을 확인!)

# 4) 모델 학습
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train_poly, y_train) # 훈련용 다항 특성으로 학습

# 5) 결정 학습
from sklearn.metrics import r2_score
y_pred = model.predict(x_test_poly) # 테스트용 다항 특성으로 예측
print('r2 :', r2_score(y_test, y_pred)) # r2 : 0.9719372415762598

# [3] 다항의 차수 늘리기 , degree = 10 , (차수N) 제곱까지 항 추가하기/생략시 2
poly = PolynomialFeatures( include_bias= False , degree= 10 )
poly.fit( x_train )
x_train_poly2 = poly.transform( x_train )
print( x_train_poly2.shape ) # 차수2 --> 차수10 증가 에 따른 (127, 9) -> (127, 285)
x_test_poly2 = poly.transform( x_test )

# 학습 후 결정계수 확인 
model = LinearRegression()
model.fit( x_train_poly2 , y_train ) # 훈련용 다항 특성으로 학습* 
from sklearn.metrics import r2_score
y_pred = model.predict( x_test_poly2 ) # 테스트용 다항 특성 으로 예측*
print( 'r2 : ' , r2_score( y_test , y_pred ) ) # r2_score( 정답지 , 예측값 )
# r2 :  0.07276663213888512
# *] 모델 구현 에서 다양한 속성값( degree= N ) 들을 테스트 하여 설계/구현 한다.
# *] 특성이 너무 많아지면 훈련 데이터가 과하게 집학하여 과대적합이 발생하여 점수가 낮아 진다.


# [4] 특성이 많아짐에 따라 특성간의 단위 표준화 (0~1)
from sklearn.preprocessing import StandardScaler
ss = StandardScaler() # 객체 생성
ss.fit(x_train_poly) # 항이 추가된 특성으로 표준화
x_train_scaled = ss.transform( x_train_poly )
x_test_scaled = ss.transform( x_test_poly )
print( x_train_poly[0] ) # [ 16.2          4.5924       ~~
print( x_train_scaled[0] ) # [-1.14878727 -1.06273398 -1.10441696  ~~
# 원본이 평균보다 작으면 음수, 

# [5] 규제: 기울기(가중치) 크기에 페널티를 부여하여 특성 오차 확인하여 특성 제외

# 1) 릿지
from sklearn.linear_model import Ridge
# ※ alpha(규제강도) : 값이 커질수록 가중치/기울기를 0에 가깝게 규제: 완만
#반복하여 최적의 규제 강도 찾기
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list :
    model = Ridge( alpha=alpha )# 강도 설정하여 릿지 모델 객체 생성
    model.fit( x_train_scaled, y_train ) # 학습
    #훈련데이터 점수와 테스트용 점수 격차 적은 alpha 찾기
    print(" --- 훈련용 학습 데이터 점수 vs 테스트용 학습 데이터 점수 --- ")
    print("Train R2: ", model.score(x_train_scaled, y_train))
    print("Test R2: ", model.score(x_test_scaled, y_test)) # alpha가 10이였을때 점수 격차가 가장 작다.

# 2) 라쏘 모델
from sklearn.linear_model import Lasso
lasso = Lasso( alpha=10) # 임의의 강도 지정 라쏘 모델 객체 생성
lasso.fit( x_train_scaled, y_train )
print( lasso.score( x_train_scaled, y_train) )
print( lasso.score( x_test_scaled, y_test) )

# 제거된 특성
import numpy as np
zero_features = np.sum( lasso.coef_ == 0)
print( '기울기 0으로 제거된 특성 수 :', zero_features)

# 특성이 적으면(과소적합/모델 단순) --> 특징을 찾기가 어렵다. PolynomialFeatures를 이용한 항 추가 할것 / degree
# 특성이 많으면(과대적합/모델 복잡) --> 규제(L1라쏘, L2릿지) / alpha