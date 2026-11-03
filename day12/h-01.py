# httpx란? 외부 api 통신하는 라이브러리, API연동 / SPRING API
# 설치 : pip install httpx
# httpx 라이브러리에는 .json 타입변환 하지만 xml을 지원하지는 않는다.
import httpx
# xmltodict란? xml을 파싱하는 라이브러라
# 설치 : pip install xmltodict
import pandas as pd

# 0) 공공데이터포털 본인 인증 키
service_key = "0f09ea9db905aeda554509024b07b553259c634233949946ad4630dd2318cc31"

# 1) 공공데이터포털에 json 형식의 자료 요청
def test1() :
    # 2) 신청한 API의 주소 및 파라미터 분석, 대구광역시 중구 맛집 현황
    url = "https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553"
    url += "?page=1"
    url += "&perPage=147"
    url += f"&serviceKey={service_key}"

    # 3) httpx 이용하여 통신하기
    # httpx.HTTP메소드명( 통신할 주소 )
    response = httpx.get( url )
    print(response)

    # 4) 응답 결과 JSON 반환, json()
    response_json = response.json()
    print(response_json)

    # 5) 판다스에 저장하기
    df = pd.DataFrame( response_json['data']) # {"currentCount:10 , "data":[실질자료]}
    df.info()

test1()

# 2) 공공데이터포털 xml 형식의 자료 요청
import xmltodict #xml 변환 라이브러리
def test2() :
    url = "https://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?"
    url += f"serviceKey={service_key}"
    url += "&pageNo=1&numOfRows=100"

    # 2. httpx 이용한 api 요청
    response = httpx.get(url)

    # 3. 요청
    response_dict = xmltodict.parse(response.text)
    # print(response_dict)

    # 4. <response> -> <body> -> <items> -> <item>
    df = pd.DataFrame( response_dict['response']['body']['items']["item"])
    df.info()
test2()



'''
[xml 파일 형태]
<response>
    <body>
        <items>
            <item>
            </item>
        </items
    <body>
</response>
'''