# Practice7 문제 [ 씨네21(Cine21) 영화 평점 및 핵심 정보 수집 ]

# 출처 및 대상: 씨네21 영화 평점 페이지, https://cine21.com/movie/point


# [1. 목표]
# Playwright의 비동기 제어와 동적 페이지네이션(click)을 활용해 여러 페이지를 순회한다.
# 영화 아이템 카드에서 제목, 이미지 링크, 전문가 평점 3가지 핵심 데이터를 정확히 추출하여 구조화한다.

# [2. 데이터 수집 요구사항]
# 2-1 (페이지 순회): 1페이지부터 3페이지까지 반복문을 통해 동적으로 페이지를 이동한다.
# 2-2 (요소 추출): 각 영화 카드 내부에서 아래 3가지 요소를 각각 수집한다.

# 제목: .title 태그의 텍스트
# 이미지: img 태그의 src 속성값
# 전문가 평점: 평점 정보가 담긴 텍스트


# 2-3 (데이터 적재): 수집된 데이터를 딕셔너리로 묶어 리스트에 저장하고 최종 출력한다.
# ====================================================================================================
import asyncio      # 비동기 라이브러리
from playwright.async_api import async_playwright # 비동기 동적 페이지 라이브러리

datas = []
async def run() : # 함수 정의
    # async_playwright() 실행 하고 끝날 때 까지 대기상태
        async with async_playwright() as p :
            # 크로미움 실행
            browser = await p.chromium.launch( headless=False)
            # 빈 페이지 열기
            page = await browser.new_page()
            # 특정 페이지 이동
            await page.goto( "https://cine21.com/movie/point" )
            # 3초 대기상태
            await page.wait_for_timeout(3000)
            # =================================================================================================================== 교수님 제공 코드
            
            # 여러개의 DOM을 반환
            page_button_list = await page.query_selector_all('.pagination .page a')
            # 반복문 3번 수행
            for i in range(1,4) :       # 1부터 3까지 반복
                await page_button_list[i - 1].click()     # 0 인덱스부터 a 마크업 클릭이벤트
                await page.wait_for_timeout( 3000 )

                items = await page.query_selector_all(".list_with_upthumb_item")
                for item in items :
                    title = await item.query_selector(".title")
                    title = await title.inner_text() if title else "제목없음"
                    img_link = await item.query_selector('.img_wrap>img')
                    img_link = await img_link.get_attribute('src') if img_link else "이미지없음"
                    score = await item.query_selector(".star_wrap > p.num")
                    score = await score.inner_text() if score else "전문가평점없음"
                    print(title, img_link, score)

                    datas.append({"제목":title, "이미지링크":img_link, "전문가 평점":score})

            # =================================================================================================================== 직접 한 방식
            # for i in range(2, 5) :
            #     items = await page.query_selector_all("#point_list_holder > div.list_with_upthumb.pc_col5_mo_col2 > div.list_with_upthumb_item")

            #     for item in items :
            #         title = await item.query_selector(".title")
            #         title = await title.inner_text() if title else "제목 없음"
            #         img = await item.query_selector( 'img.img_thumb' )
            #         img = await img.get_attribute('src') if img else '이미지없음'
            #         score = await item.query_selector('.star_wrap.justify_center.mo_xs > .num')
            #         score = await score.inner_text() if score else "점수없음"

            #         datas.append({"제목":title, "이미지링크":img, "전문가 평점":score})

            #     next_page = await page.query_selector(f'div.pagination > div.page > a[href="javascript:fetch_point_list({i})"]')
            #     await next_page.click()
            #     await page.wait_for_timeout(3000)
            # ===================================================================================================================
   
            print(datas)
            await browser.close()

asyncio.run(run())