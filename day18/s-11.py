import pandas as pd
url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
df = pd.read_csv(url)

X = df[['alcohol', 'sugar', 'pH']]
Y = df['class']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)

## 1) lightGBM : LGBMClassifier 분류모델 / LGBMRegressor 회귀모델
from lightgbm import LGBMClassifier # 0레드 / 1 화이트 ->> 와인 종류 분류
model = LGBMClassifier(
    # 다양한 매개변수 설정
    n_estimators = 1000,      # 추정기(몇 번 학습을 할 것인가, 기본값 100이며 보통 1000~3000 설정)
    learning_rate=0.05,      # 학습률(각 트리의 축소 비율), 기본값 0.1 -> 0.05만큼의 가중치(기울기)만큼 이전 트리의 오차를 보완하는 학습 보폭 설정
    num_leaves=15,           # 하나의 트리(모델)가 가질 수 있는 최대 리프 노드 수( 성능결정, 과적합 억제하는 1순위 튜닝 변수 )
    max_depth=10,             # 하나의 트리 최대 깊이, 특정 가지만 비정상적으로 깊어지는 것을 방지. 기본값 -1(무제한)
    min_child_samples=20,    # 리프 노드의 최소 샘플 수( 과적합 방지용 ), 기본값 20
    subsample=0.8,           # 매 트리 학습마다 랜덤으로 선정된 80%의 데이터만 가지고 학습하겠다
    subsample_freq=1,        # subsample을 몇 번의 트리마다 실행할지 결정(0이면 subsample 설정해도 작동 X)
    colsample_bytree=0.8,    # 매 학습마다 랜덤으로 전체 특성 중 80%만 무작위 선택 학습 
    class_weight="balanced", # 분류 모델에서 타깃/종속 변수에 비율 불균형 보정(데이터가 균등하면 생략 -> None)
    verbose=-1,              # 매 학습마다 로그 숨김
    random_state=42, n_jobs=-1,
)

from lightgbm import early_stopping
# 2) 모델 학습 수행
# eval_set=[ (X_test, Y_test) ]: 조기 종료 하기위한 (성능) 검증용 데이터셋 포함
# - 만약에 여러번 학습 중에 손실함수 결과 오차/잔차가 최적이 되면 종료 모니터링
# callbacks=[ early_stopping( stopping_rounds=50, verbose=False) ] -> 학습 과정 중 실행할 콜백 함수
# - 학습 마다 검증 성능이 개선되지 않을 때 추가로 기다릴 반복 횟수
model.fit( X_train, Y_train, 
        eval_set=[ ( X_test, Y_test ) ],
        callbacks=[ early_stopping( stopping_rounds=50, verbose=False) ]
)

# 3) 주요 속성 확인
print(model._best_iteration)        # 최적의 트리 반복 수/번호      # 100
best = model.best_iteration_

print(model.feature_name_)          # 각 특성의 이름                # ['alcohol', 'sugar', 'pH']
print(model.feature_importances_)   # 각 특성의 중요도              # [138 824 438]

# 4) 평가지표
from sklearn.metrics import f1_score
Y_pred = model.predict(X_test)
print(model.score(X_train, Y_train))                
print(model.score(X_test, Y_test))
print(f1_score(Y_test, Y_pred, average='macro'))    
# 0.8537617856455647
# 0.8353846153846154 # 학습 -> 테스트 -> 0.03 -> 3%(10% 아래로 과적합 억제)
# 0.8031590774656059


# 만약 max_depth=6 -> 10이 된다면? 파라미터 수정 시 성능 떨어짐
# 0.8864729651722147
# 0.8530769230769231
# 0.8197484027443542

# 5) 예측하기
new_wine = pd.DataFrame([ [11.5, 2.3, 3.1], [13.8, 11.2, 3.3] ])
new_pred = model.predict( new_wine )
print('예측 1:', new_pred[0])   # 예측 1: 0.0 ->> 레드 와인
print('예측 2:', new_pred[1])   # 예측 2: 1.0 ->> 화이트 와인