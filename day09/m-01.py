# Matplotlib & Seaborn

#맷플롯립:
# 개발자 : 코딩능력 , 분석가 : 차트해석능력
# 설치 : pip install matplotlib
# 확인
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
print(matplotlib.__version__)
# 맷플롯립 그래프는 한글 지원 X
# #### 한글 폰트 설정 ####
import matplotlib.pyplot as plt
plt.rc( 'font' , family = 'Malgun Gothic') # 윈도우 맑은고딕으로 변경
plt.rcParams['axes.unicode_minus'] = False # 음수 기호 깨짐 방지

# [1] 선 차트
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_loss = [0.9, 0.7, 0.55, 0.45, 0.38, 0.32, 0.28, 0.25, 0.23, 0.20]
val_loss = [0.95, 0.75, 0.60, 0.52, 0.48, 0.45, 0.44, 0.43, 0.44, 0.45]

# 1) 차트의 전체 크기 설정 : pit.figure( figsize = ( 가로inch, 세로inch ) )
plt.figure( figsize=( 7,4 ))


# 2) 선 차트 : plt.plot( x축값, y축값, label = "계열명", color="색상명", linestyle="선종류", marker='점 종류')
plt.plot( epochs, train_loss , label="Train Loss", color="blue", linestyle="-", marker="o")
plt.plot( epochs, val_loss , label="값 손실", color="red", linestyle="--", marker="s")
plt.title('Epoch별 모델 손실값(Loss) 추세')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend() # 범례 표시

# plt # 맷플롯립 별칭
plt.show() # 차트 실행


# ======================================================================================================================
# [2] 막대 그래프(비교) , 선 차트(추세) plt.plot
classes = ['Cat', 'Dog', 'Bird', 'Fish']
counts = [120, 150, 80, 45]

# 1) plt.bar( x값, y값, color=[색상], width=막대크기)
bars = plt.bar( classes, counts, width=0.5,
               color = [ '#222222', '#444444', '#666666', '#888888'] )

# 2) 막대 값 레이블
# plt.bar_label( 막대차트변수, padding=막대와레이블간격, fontsize=폰트크기 )
plt.bar_label( bars, padding=3, fontsize=8)
plt.title('클래스별 샘플수')
plt.xlabel('클래스')
plt.ylabel('샘플 수')
plt.grid(True, alpha = 0.2) # alpha = "투명도"

plt.show()

# ======================================================================================================================
# [3] 산점도 (산점관계)
x = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
y = np.array([2.3, 3.8, 5.1, 7.0, 7.8, 9.2, 10.5])

# 1) 산점도 그래프
# plt.scatter( x축값, y축값, color="색상", s = 점크기, alpha = 투명도 )
plt.scatter( x, y, color= "purple", s = 80, alpha = 0.8 )
plt.title("공부시간과 시험점수의 상관관계")
plt.xlabel('공부 시간')
plt.ylabel('시험 점수')
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()

# ======================================================================================================================
# [4] 히스토그램( 연속형 수치/값 분표 )

# 평균 170을 중심으로 표준편차 5만큼 처져 있는 종모양(가우시안 분포)의 연속형 가상 데이터 1000개 무작위 생성
heights = np.random.normal(loc=170, scale=5, size=1000)

# 1) 히스토그램 -> plt.hist(값, bins="구간개수", color='색깔', edgecolor='테두리색깔', alpha="투명도")
plt.figure(figsize=(6, 4))
plt.hist(heights, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('키(Height) 데이터의 정규분포 확인')
plt.xlabel('키 (cm)')
plt.ylabel('빈도/분포 수')
plt.grid(axis='y', linestyle=':', alpha=0.6)

plt.show()