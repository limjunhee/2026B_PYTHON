# Practice8: API 데이터 수집
# 1. 개요 및 대상 API 정보
# API 이름: 행정안전부_착한가격업소 현황
# API URL: https://www.data.go.kr/data/3045247/fileData.do 

# 목표: httpx를 통해 공공데이터 API를 호출하고, pandas를 활용해 업소명, 주소, 가격 데이터를 구조화한 뒤 통계 분석을 수행합니다.
# 2. 상세 요구사항
# 2-1 (API 호출 및 파라미터 설정):
# 지정된 API URL에 인증키(serviceKey)를 포함하여 요청합니다.
# 임의의 100건의 데이터를 수집

# 2-2 (데이터프레임 적재):
# 응답받은 JSON 데이터 중 실제 행 목록인 data 배열을 추출하여 pandas.DataFrame으로 변환합니다.

# 2-3 (데이터 전처리 및 분석):
# 가격1 컬럼의 데이터를 숫자형(pd.to_numeric)으로 변환합니다.
# 수집된 100건 데이터 기준 가격1의 평균값을 산출하여 출력합니다.

# 2-4 (업종별 평균 가격 집계 및 시각화):
# groupby('업종')을 사용하여 업종별 가격1의 평균 가격을 계산합니다.
# seaborn의 barplot 활용하여 업종별 평균 가격 비교 막대그래프를 시각화합니다.
# =========================================================================================
import httpx
import pandas as pd
import seaborn as sns
# 내 인증키
service_key = "0f09ea9db905aeda554509024b07b553259c634233949946ad4630dd2318cc31"

def practice8() :
    url = "https://api.odcloud.kr/api/3045247/v1/uddi:0d236000-b33f-41ad-9227-ee0efa3ec6c8"
    url += "?page=1&perPage=100"
    url += f"&serviceKey={service_key}"

    response = httpx.get(url)                   # print(response)
    response_json = response.json()
    print(response_json)
    print(type(response_json)) # dict
    
    df = pd.DataFrame( response_json['data'])   
    #print(type(df))
    new_df = pd.to_numeric(df["가격1"])
    print(new_df)
    print(type(new_df))
    print(new_df.mean()) # 2-3 평균값
    

    new_df = df.groupby('업종')['가격1'].mean()

    sns.barplot

    
practice8()