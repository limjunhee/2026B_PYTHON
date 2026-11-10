import pandas as pd
df = pd.read_csv('./day14/fish.csv')

# 1) 이진 분류 실습하기 위한 정답지 2개 사용
df = df[ (df['Species'] == 'Bream') | (df['Species'] == 'Smelt')]
X = df[['Weight','Length1','Length2','Length3','Height','Width']] # 6가지의 특성
Y = df['Species'] # Bream or Smelt

# 2) 분리
# stratify = Y : 타깃 무작위 분리 한 경우 타깃의 클래스(값) 비율 일정 유지, 분류모델
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size = 0.2, random_state = 42, stratify = Y
)

# 3) 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_scaled = ss.transform( X_train )
X_test_scaled = ss.transform( X_test )

# 4) 로지스틱 모델 사용
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit( X_train_scaled, Y_train)
Y_pred = model.predict(X_test_scaled)
print(Y_pred) # ['Bream' 'Bream' 'Smelt' 'Bream' 'Bream' 'Smelt' 'Smelt' 'Bream' 'Bream' 'Bream']

# 5) 결과 속성
print(model.classes_) # 정답지 종류 -> ['Bream' 'Smelt']
print(model.predict_proba(X_train_scaled[:3])) # 확률 반환
# [[0.99396167 0.00603833]      # Bream(1열) , Smelt(2열)
#  [0.03311198 0.96688802]
#  [0.98732805 0.01267195]]