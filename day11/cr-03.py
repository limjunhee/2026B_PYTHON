# 동적 페이지 라이브러리 설치 : python -m pip install playwright
# playwright - 셀레니움과 비슷한 동적 페이지 조작 라이브러리
# playwright install # 크롬(구글회사브라우저)과 비슷한 백르아룬드 브라우저( 크로미움 ) 설치

import asyncio      # 비동기 라이브러리
from playwright.async_api import async_playwright # 비동기 동적 페이지 라이브러리

# 예제3) 동적 페이지 크롤링 -> 대기/이벤트 존재하는 페이지
# 1) 크롤링할 페이지 주소 가져와서 파라미터 분석 -> ssc = 검색결과 탭 , query = 검색어
url = "https://search.naver.com/search.naver?ssc=tab.image.all&query=짱구"

# 2) 비동기 함수 만들기
# async def 함수명() : # 함수 선언하고 동기화
async def run() :
    # 2-1) async_playwright() 실행하고 종료되기 전까지 동기화 처리
    async with async_playwright() as p :
        
        # 2-2) 크로미움(구글에서 제공하는 백그라운드 브라우저)
        # await p.chromium.launch( headless = True(백그라운드)/False(뷰모드) )
        browser = await p.chromium.launch( headless = False )

        # 2-3) 현재 실행된 크로미움의 새로운 페이지(빈 페이지) 열기
        page = await browser.new_page()
        
        # 2-4) 빈 페이지에 특정한 URL 주소 대입/이동
        await page.goto( url )

# *** asyncio.run( 동기화함수() ) ***
asyncio.run( run() )