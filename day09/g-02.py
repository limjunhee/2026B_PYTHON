# 시본(seaborn) : 맷플롭릿 기반의 시각화 라이브러리
# 설치 : pip install seaborn

import seaborn as sns
# print(sns.__version__)

# 0) 실습 자료
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 윈도우 기준 한글 폰트 설정 및 마이너스 부호 깨짐 방지
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 시본 기본 테마 적용 (폰트 설정 유지)
sns.set_theme(font='Malgun Gothic', rc={'axes.unicode_minus': False}, style='whitegrid')

np.random.seed(42)
n = 100
df = pd.DataFrame({
  '나이': np.random.randint(20, 60, size=n),
  '소득': np.random.randint(2500, 9000, size=n),
  '신용점수': np.random.randint(500, 850, size=n),
  '멤버십': np.random.choice(['일반', 'VIP'], size=n, p=[0.7, 0.3]),
  '이탈여부': np.random.choice([0, 1], size=n, p=[0.75, 0.25]) # 0: 유지, 1: 이탈
})
# 나이가 많을수록 소득이 높은 경향 부여
df['소득'] += df['나이'] * 40

# ======================================================================

# 1) 카운트플롯 (범주형 빈도 집계)
# sns:seaborn의 별칭
# sns.countplot( data=데이터프레임 , x = '범주형컬럼명', hue="빈도컬럼명", palette="색상테마")
sns.countplot( data = df, x = "멤버십", hue="이탈여부", palette="Set1") 
plt.title('멤버십별 이탈빈도')

# 범례
plt.legend( title = "이탈 여부", labels = ['유지(0)', '이탈(1)'] )


plt.show()

# ======================================================================
# 2) 박스플롯 ( 범주형 수치 분포 )
# sns.boxplot( data=데이터프레임, x="범주형컬럼명", y="수치형컬럼명", hue="그룹컬럼명", palette="색상테마")
sns.boxplot( data=df, x="멤버십", y="소득", hue="이탈여부", palette="Pastel2")
plt.title("멤버십 이탈 여부에 따른 소득 분포")
plt.show()



# ======================================================================
# 3) 히트맵 ( 서로 다른 변수들 간의 상관관계 파악 )
# 상관계수 : 하나의 변수의 값이 변하면 다른 변수의 값은 증가/감소 관계 수치화 (-1(음) / 1(양))
# 0.85이상 -> 관계가 있다
# 데이터프레임.corr() #상관계수 행렬 계산
# 문자열(범주형) 제외한 수치형만 추출

numeric_df = df[ ['나이', '소득', '신용점수'] ]   # 연속형 수치 변수만 선택할 경우
corr_matrix = numeric_df.corr()          # 피어슨 상관계수 행렬 계산

# 1) 히트맵
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('수치형 특성 간 상관계수 히트맵')

plt.show()

# ======================================================================
# 4) 산점도, sns.scatterplot( data=데이터프레임, x="수치컬럼명" , y="수치컬럼명", hue="그룹컬럼명")

sns.scatterplot(data=df, x='나이', y='소득', hue='이탈여부')
plt.title(" 나이 vs 소득 산점도 ")
plt.show()

# ======================================================================
# 5) 페어플롯, 
sns.pairplot(df, hue='이탈여부', palette='Set1')
plt.show()