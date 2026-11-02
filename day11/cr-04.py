
import asyncio      # 비동기 라이브러리
from playwright.async_api import async_playwright # 비동기 동적 페이지 라이브러리

# 예제 4) 동적 페이지 크롤링
# 1) 중고나라 제품 크롤링 , url = "https://web.joongna.com/search/"

async def run() : # 함수 정의
    keyword = input("중고 제품명 : ")
    min_price = input("최소 가격 입력 : ")
    max_price = input("최대 가격 입력 : ")

    # 2~5번까지는 코드가 크게 바뀔 일이 없으므로 복사해서 써도 좋음.
    # 2) async_playwright() 실행 하고 끝날 때 까지 대기상태
    async with async_playwright() as p :
        # 3) 크로미움 실행
        browser = await p.chromium.launch( headless=False)
        # 4) 빈 페이지 열기
        page = await browser.new_page()
        # 5) 특정 페이지 이동
        await page.goto( f"https://web.joongna.com/search/{keyword}" )
        # 6) 3초 대기상태
        await page.wait_for_timeout(3000)
        # 7) 입력받은 값을 웹 페이지에 채우기
        # page.get_by_속성명("속성값")
        # DOM.fill( 값 )        # 속성값 대입
        # await page.get_by_placeholder("최소 가격").fill(min_price) -> placeholder가 '최소 가격'이면 입력받은 값을 대입
        await page.get_by_placeholder("최소 가격").fill(min_price) # html placeholder 이용하여 특정 마크업 식별
        await page.wait_for_timeout( 1000 ) # 1초간 일시정지

        await page.get_by_placeholder("최대 가격").fill(max_price) # -> placeholder가 '최대 가격이면 입력받은 값을 대입
        await page.wait_for_timeout( 1000 ) # 1초간 일시정지

        # 8) 특정한 마크업 클릭 이벤트 실행, Dom.click()
        await page.get_by_text("적용").click() # 텍스트 "적용" 갖고 있는 마크업 선택
        await page.wait_for_timeout( 3000 )

        # 9) 제품 사진, 제품명, 제품가격 추출
        # href^ : '/시작주소/ : 시작주소로 시작하는 모든 주소를 식별
        items = await page.query_selector_all("div.group > div > a[href^='/product']")
        # print(items)
        for item in items :
            title = await item.query_selector(".typo-body-sm-medium-14")
            title = await title.inner_text() if title else "제품명 없음"
            price = await item.query_selector(".typo-title-lg-semibold-18")
            price = await price.inner_text() if price else "제품가격 없음"
            img = await item.query_selector('img')
            img = await img.get_attribute( 'src' ) if img else "이미지 없음"
            print(title, price, img)

        # 10) 브라우저 종료
        await browser.close()

asyncio.run(run()) # 함수 실행