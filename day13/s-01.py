# 사이킷 런 -> 방대한 머신러닝 알고리즘 모델 제공하는 라이브러리
# python -m pip install scikit-learn

# 머신러닝의 목표 -> 추론/예측 과정
# 특성 : 모델이 학습하는 자료 정보, 타깃 : 모델이 궁극적으로 맞춰야 하는 정답 정보

# 실습에서 이용한 자료 : https://www.kaggle.com/datasets/vipullrathod/fish-market 에서 Fish.csv 다운로드


# 지도학습 : 특성과 타깃을 모두 제공하며 학습시키는 방법 -> 회귀/분류
# 비지도학습 : 타깃을 제공하지 않고 특성만 제공하는 학습 -> 군집(집합)/텍스트마이닝

# [1] 단순 선형 회귀
# 1-1. 판다스로 자료 불러오기
import pandas as pd
df = pd.read_csv('./day13/Fish.csv')
df.info()

# 1-2. 모델 학습에 사용할 데이터 추출
feature = ['Length2'] # 특성 : Length2 (물고기의 대각선 cm) -> 사이킷런 모델 구조상 학습할 특성은 2차원 배열이여야 함
target = 'Weight'       # 타깃 : Weight (물고기의 무게 g)

# 1-3. 독립변수/입력변수/특성/x , 
x = df[feature] # 2차원 -> <class 'pandas.DataFrame'>
y = df[target]  # 1차원 -> <class 'pandas.Series'>

# 1-4. 데이터 분리, 학습용/테스트용 나누기, 학습과 평가/예측성능 자료 구분
from sklearn.model_selection import train_test_split
# 특성학습자료, 특성테스트자료, 타깃학습자료, 타깃테스트자료 = train_test_split( 특성, 타깃, test_size=비율, random_state=난수시드값)
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state = 42 )
# 훈련 세트 : 모델에서 규칙을 찾는 자료
# 테스트 세트 : 모델 학습 후 모델 평가/예측성능 점수/지표

# 1-5. 단순(특성값 1개) 선형회귀 모델
from sklearn.linear_model import LinearRegression
model = LinearRegression() # 파이썬에서 객체 생성 방법, 변수명 = 클래스명()

# 1-6. 모델 학습, model.fit( 특성자료, 타깃자료)
model.fit(x_train, y_train)

# 1-7. 모델 가중치(기울기) -> model.coef_
print(model.coef_) # [30.43452394]

# 1-8. 모델 편향( y 절편 편향값) 확인
print(model.intercept_) # -477.30634978973194 (음수 나오는 경우 모델에 문제 있음, 일단 실습이니 넘어감)

# 1-9. 학습한 모델의 예측, 새로운 x값을 넣어서 y값 구하기, model.predict( 2차원특성자료 )
print(model.predict( [[30]] )) # 물고기 길이가 30일 때 무게를 예측 -> [435.72936841]
    # ※ 단순 회귀모델 : y =ax+b -> [30.43452394] * [30] + [-477.30634978973194]
    # ※ 문제점 : 직선 관계는 한계가 존재


# 1-10. 시각화
import matplotlib.pyplot as plt
plt.scatter( [x_train], y_train ) # 학습 자료들
plt.scatter( [30], model.predict([[30]]), color = 'red' ) # 길이가 30일 때 나오는 무게값(빨간색 점으로 하나 찍힘)
plt.plot( [0, 100], model.predict([[0],[100]]) )
plt.show()

# 1-11. 문제점
# x, y가 직전 관계이며 실 자료들은 꼭 비례 증가가 아닐 수 있다.
# 다항 회귀로 확장하여 특성을 추가한다.

# 1-12 모델 평가, 테스트용 자료 사용
y_pred = model.predict( x_test )
# 평균 제곱근 오차계산
import numpy as np # sqrt(제곱근) 넘파이 함수 사용
from sklearn.metrics import mean_squared_error # 평균 오차( 학습자료와 테스트자료 )
rmse = np.sqrt( mean_squared_error( y_test, y_pred) )
print("rmse", ":", rmse) # rmse : 160.01413830813442
# 해석 : 모델이 실제 무게와 얼마나 틀렸는지 평균 오차

# 결정계수(R SCORE) : 타깃 데이터의 전체 변동성 대비 모델이 얼마나 잘 설명하는지 0~1 사이의 비율로 알려줌
from sklearn.metrics import r2_score #결정계수
r2 = r2_score( y_test, y_pred ) # 정답지와 예측값
print("r2 :", r2) # r2 : 0.8199897860284712 -> 1에 가까울수록 모델이 잘 설명한다. 현재는 약 82% 정도 설명한다. (18%는 모델이 설명하지 못함)