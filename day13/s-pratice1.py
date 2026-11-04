# 1. 데이터 준비

#  - Seaborn 내장 데이터셋인 'tips'를 불러옵니다.

#   import seaborn as sns

#   df = sns.load_dataset('tips')

#  - 독립변수(X, 문제지): 식사 총액 'total_bill' 컬럼 (반드시 2차원 DataFrame 구조 유지)

#  - 종속변수(Y, 정답지): 팁 'tip' 컬럼 (1차원 Series 구조 유지)


# 2. 데이터 분할

#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.

#  - 재현성을 위해 random_state=42로 고정합니다.


# 3. 모델 학습 및 수학적 파라미터 확인 

#  - Scikit-learn의 LinearRegression 모델을 생성하고 훈련 데이터로 학습시킵니다.

#  - 학습 완료 후 모델이 도출한 '기울기(model.coef_)'와 'y절편(model.intercept_)'을 출력하세요.


# 4. 성능 평가 및 신규 데이터 예측

#  - 테스트 세트(X_test)에 대한 예측값(Y_pred)을 생성하세요.

#  - 실제값(Y_test)과 예측값(Y_pred)을 비교하여 R²(결정계수)와 RMSE(평균 제곱근 오차)를 산출하고소수점 둘째 자리까지 출력하세요.

#  - 만약 식사 총액이 $30, $100인 새로운 손님이 방문했을 때, 예상되는 팁 금액을 각각 예측하여 출력하세요.


# 5. 결과 시각화 및 한계점 분석 

#  - Matplotlib을 활용하여 아래 3가지 요소를 하나의 차트에 시각화하세요:

#   ① 테스트 세트의 실제 데이터 산점도 (X_test vs Y_test)

#   ② 식사비 $5부터 $100까지 모델이 예측한 선형 회귀선

#   ③ 식사비 $50일 때의 모델 예측 지점 (붉은 점으로 강조)

# ===================================================================================================================
# 1. 데이터 준비
import seaborn as sns
df = sns.load_dataset('tips')
print(df)
feature = ['total_bill']
target = 'tip'
x = df[feature]
y = df[target]

# 2. 데이터 분할
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state = 42 )

# 3. 모델 학습 및 수학적 파라미터 확인
from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(x_train, y_train) # 모델 학습
print(model.coef_) # 모델 가중치(기울기) 확인 -> [0.10696371]
print(model.intercept_) # 모델 편향(y 절편값) 확인 -> 0.9252355585570546

# 4. 성능 평가 및 신규 데이터 예측
y_pred = model.predict(x_test) # 테스트 세트에 대한 예측값 생성

# 결정 계수 출력(R2 SCORE)
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred) # 정답지, 예측값
print("결정계수 :", round(r2,2))

# 평균 제곱근 오차(RMSE)
import numpy as np # sqrt 제곱근 넘파이 함수 사용하기 위해 임포트
from sklearn.metrics import mean_squared_error # 평균 오차(학습자료, 테스트자료)
rmse = np.sqrt( mean_squared_error( y_test, y_pred ))
print("평균 제곱근 오차 :", round(rmse,2))

# 식사 총액이 30, 100달러인 새로운 손님 방문시 예상되는 팁 금액 각각 예측해서 출력하기
print(model.predict([[30]])) # [4.13414676]
print(model.predict([[100]])) # [11.62160624]

# 5. 결과 시각화 및 한계점 분석
import matplotlib.pyplot as plt
plt.scatter([x_test], y_test, color ="skyblue") # 테스트 데이터들
plt.plot( [5,100], model.predict([[5],[100]]), color = 'black') # 식사비 5~100까지 모델이 예측한 선형 회귀선
plt.scatter( [50], model.predict([[50]]), color = 'red') # 식사비가 50일 경우 모델 예측 지점(붉은점)
plt.show()