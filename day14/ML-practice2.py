# PythonML Practice 2: 다항 규제 회귀 기반 성적 예측
# 데이터 출처: https://www.kaggle.com/datasets/shambhurajejagadale/student-performance-prediction-dataset
# 1. 데이터 준비 및 전처리
#  - Kaggle 데이터셋을 불러옵니다.
#    import pandas as pd
#    df = pd.read_csv('./student_dataset_10000_rows.csv')
#  - 범주형 변수를 제외한 6개 수치형 컬럼을 독립변수(X, 문제지)로 추출하세요:
#    ['study_hours', 'attendance', 'sleep_hours', 'internet_usage', 'assignments_completed', 'previous_score']
#  - 시험 성적인 'exam_score' 컬럼을 종속변수(Y, 정답지)로 설정하세요.

# 2. 데이터 분할
#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
#  - 재현성을 위해 random_state=42로 고정합니다.

# 3. 다항 특성 확장 및 표준화 (고정 차수: degree=2)
#  - PolynomialFeatures(degree=2, include_bias=False)를 사용하여 2차 다항 특성을 생성하세요.
#    * 훈련 세트(X_train)로만 .fit()을 수행하고, X_train과 X_test를 각각 .transform() 하세요.
#  - StandardScaler를 생성하고, 다항 확장된 훈련 세트(X_train_poly) 기준으로 .fit()한 뒤 표준 점수로 변환하세요.
#    * 특성 간 스케일 차이를 맞추기 위해 훈련 세트와 테스트 세트 모두 .transform() 하세요.

# 4. 3가지 모델 학습 및 결정계수(R²) 비교 (고정 규제: alpha=1.0)
#  - 3가지 회귀 모델을 각각 생성하고 스케일링된 훈련 데이터로 학습시키세요:
#    1) LinearRegression()
#    2) Ridge(alpha=1.0, random_state=42)
#    3) Lasso(alpha=1.0, random_state=42)
#  - 각 모델별 훈련 세트 R² 점수(Train R²)와 테스트 세트 R² 점수(Test R²)를 각각 산출하여 비교 출력하세요.

# 5. 임의 대조군 데이터에 대한 3가지 모델 예측 비교
#  - 아래 대조군 샘플 2개를 준비하세요:
#    * 샘플 1 (상위권): study_hours=9, attendance=95, sleep_hours=7, internet_usage=2, assignments_completed=18, previous_score=85
#    * 샘플 2 (하위권): study_hours=2, attendance=60, sleep_hours=5, internet_usage=9, assignments_completed=4, previous_score=50
#  - 각 샘플 데이터를 앞서 학습시킨 동일한 변환기(PolynomialFeatures, StandardScaler)로 변환하세요.
#  - 3가지 모델(LinearRegression, Ridge, Lasso)에 변환된 데이터를 각각 대입하여 예상 시험 성적을 산출하고 비교 출력하세요.


# ================================================================================================================
# [1] 데이터 준비 및 전처리
import pandas as pd
df = pd.read_csv("./day14/student_dataset_10000_rows.csv")
df.info()

X = df[['study_hours', 'attendance', 'sleep_hours', 'internet_usage', 'assignments_completed', 'previous_score']]
Y = df['exam_score']

# [2] 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y,test_size=0.2, random_state=42 )

# [3] 다항 특성 확장 및 표준화
# 2차 다항 특성 생성하기
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)

# 다항 확장된 훈련 세트 기준으로 .fit()하고 표준 점수로 변환하기
from sklearn.preprocessing import StandardScaler
ss = StandardScaler() # 객체 생성
ss.fit(X_train_poly)
X_train_scaled = ss.transform( X_train_poly )
X_test_scaled = ss.transform( X_test_poly )

# [4] 3가지 모델 학습 및 결정계수(r2) 비교 (고정 규제 alpha = 1.0)
from sklearn.linear_model import LinearRegression
model_linear = LinearRegression()
model_linear.fit(X_train_scaled, Y_train)
model_linear_test_pred = model_linear.predict(X_test_scaled)
model_linear_train_pred = model_linear.predict(X_train_scaled)

from sklearn.linear_model import Ridge
model_ridge = Ridge( alpha=1.0, random_state=42)
model_ridge.fit(X_train_scaled, Y_train)
model_ridge_test_pred = model_ridge.predict(X_test_scaled)
model_ridge_train_pred = model_ridge.predict(X_train_scaled)

from sklearn.linear_model import Lasso
model_lasso = Lasso(alpha=1.0, random_state=42)
model_lasso.fit(X_train_scaled, Y_train)
model_lasso_train_pred = model_lasso.predict(X_train_scaled)
model_lasso_test_pred = model_lasso.predict(X_test_scaled)

from sklearn.metrics import r2_score
print(" --- 세 가지 모델별 훈련 세트, 테스트 세트 R2 점수 산출 결과 --- ")
print("선형 모델 훈련용 r2: ", r2_score(Y_train, model_linear_train_pred))
print("선형 모델 테스트용 r2: ",r2_score(Y_test, model_linear_test_pred))
print("릿지 모델 훈련용 r2: ", r2_score(Y_train, model_ridge_train_pred))
print("릿지 모델 테스트용 r2: ", r2_score(Y_test, model_ridge_test_pred))
print("라쏘 모델 훈련용 r2: ", r2_score(Y_train, model_lasso_train_pred))
print("라쏘 모델 테스트용 r2: ", r2_score(Y_test, model_lasso_test_pred))

# [5] 임의 대조군 데이터에 대한 3가지 모델 비교
new_data = [[9,95,7,2,18,85], [2,60,5,9,4,50]]
new_data_poly = poly.transform(new_data)
new_data_scaled = ss.transform( new_data_poly )

new_data_linear_pred = model_linear.predict(new_data_scaled)
new_data_lasso_pred = model_lasso.predict(new_data_scaled)
new_data_ridge_pred = model_ridge.predict(new_data_scaled)

print("선형 모델 결과: ", new_data_linear_pred)
print("라쏘 모델 결과: ", new_data_lasso_pred)
print("릿지 모델 결과: ", new_data_ridge_pred)

# 파일 불러오기 df = pd.read_csv('파일경로') -> 
# 독립변수(X, Y) 선언 X = df[['열이름']] , Y = df['열이름'] -> 
# 데이터 분할(훈련:테스트 비율)  -> 
# 다항 특성 확장 PolynomialFeatures ->
# 표준 점수 변환(표준화) StandardScaler ->
# 모델 선택 후 학습 LinearRegression, Ridge, Lasso 선택하고 predict() ->
# 결정계수(r2) 구하기 r2_score