# 웹 크롤링: 웹페이지에 존제하는 데이터들을 수집하는 기술
# HTML/CSS 기초 지식 필요 (식별자를 볼 수 있으면 됨)
# 파이썬 크롤링 라이브러리 : 
    # 정적( request / BeautifulSoup )
    # 동적( Seleium / Playwright ) 등

# 확인
    # 1. 크롤링할 페이지의 도메인주소/robots.txt 접속하여 크롤링 허용 여부를 확인
    # https://www.jobkorea.co.kr/robots.txt
    # User-agent: 사용자/브라우저/AI , Disallow: 불가능 , allow : 가능
    # 2. 개발자도구(F12) -> ctrl+shift+c -> 크롤링 요소 선택 -> 선택자/식별자 확인

# 설치 : python -m pip install requests
# 설치 : python -m pip install beautifulsoup4

# 1) 네이버 검색 정보 크롤링 , *파라미터 정리* , ? -> 쿼리스트링
url = "https://search.naver.com/search.naver?query=안양날씨"

# 2) requests 라이브러리로 해당 주소 요청
import requests                     # URL 요청 라이브러리
response = requests.get(url)        # requests.get("요청할 주소")
# print(response)                     # <Response [200]> -> 200, 통신 정상!
# print(response.text)

# 3) 요청 성공했으면 요청한 페이지의 HTML 파싱하기.
from bs4 import BeautifulSoup # 요청된 URL의 HTML 파싱 라이브러리

# BeautifulSoup( 요청한 결과의 내용물 , "html.parser" )
soup = BeautifulSoup(response.text, "html.parser")

# 4) 파싱한 이유 : 특정한 식별자(마크업)의 텍스트/정보 추출
#soup.select(선택자) : 여러 개 추출 # soup.select_one(선택자) : 한개 추출
text = soup.select_one(".temperature_text") 
print(text) # <div class="temperature_text"> <strong><span class="blind">현재 온도</span>15.2<span class="celsius">°</span></strong> </div>

# 5) 마크업 사이의 텍스트 추출
print( text.get_text() ) # 현재 온도15.2°