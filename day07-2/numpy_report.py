import numpy as np

text = np.genfromtxt('./day07-2/한국도로교통공단_부문별 노인 교통사고 통계_20181231.csv',
                     delimiter=',', skip_header=1, dtype=str, encoding='cp949')

region = text[:, 0:2]                     # [시도, 시군구]
data = text[:, 2:].astype(np.float64)     # 숫자 6개 열
print(data.shape)  # (229, 6) -> 229개 지역, 6개 열

# -------------------------------------------------------------------------------
# 1) 시군구별 노인 교통사고 발생건수의 평균값, 최댓값
accidents = data[:, 0]                       # data의 첫번째 열 → 각 시군구별 사고 발생건수
print(int(np.mean(accidents)))               # 사고 발생건수 평균 : 168
print(int(np.max(accidents)))                # 최대 발생건수 : 785

# -------------------------------------------------------------------------------
# 2) 발생건수 300 이상 이거나(|) 사망자수 15명 이상인 지역 추출, 지역 수
risk = region[(data[:,0] >= 300) | (data[:,1] >= 15)] 
print(risk) # 지역 이름 출력
print(len(risk)) # 42곳

# -------------------------------------------------------------------------------
# 3) 사고 100건당 사망자수(치사율) 배열 생성, 가장 높은 지역
fatality = data[:, 1] / data[:, 0] * 100
print(region[np.argmax(fatality)])      # ['전북' '고창군']
print(np.max(fatality))                 # 27.27...

# -------------------------------------------------------------------------------
# 4) 발생건수 200 이상 이면서(&) 부상자 대비 경상 비율 60% 이상인 지역의 비중(%)
light_ratio = data[:, 4] / data[:, 2] * 100
group = data[(data[:, 0] >= 200) & (light_ratio >= 60)]
print(len(group))                       # 21
print(len(group) / len(data) * 100)     # 9.17...

# -------------------------------------------------------------------------------
# 5) 사망자수를 정규화(0 ~ 1)한 후 정규화한 값이 0.9 이상인 '최우선 관리 지역'의 전체 정보를 추출
deaths = data[:, 1]
norm = (deaths - np.min(deaths)) / (np.max(deaths) - np.min(deaths))

top = text[norm >= 0.9]                 # 지역명까지 포함된 전체 정보
print(len(top))                         # 3

# 사망자수 기준 내림차순 정렬 (text에서 사망자수는 3번 열)
order = np.argsort(top[:, 3].astype(np.float64))[::-1]
print(top[order])

# [['경북' '포항시' '536' '32' ...]
#  ['경남' '창원시(통합)' '527' '31' ...]
#  ['충북' '청주시' '785' '30' ...]]