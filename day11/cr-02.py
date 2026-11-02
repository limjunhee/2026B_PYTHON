# 예제2) 동적 페이지 크롤링( 페이징 처리 )
# 예스24 베스트셀러 도서 정보 크롤링 / 페이징처리(반복문)
import requests
from bs4 import BeautifulSoup

book_list = [ ]
# 1) 크롤링한 주소 불러오기. 정리/분석 -> categoty: 001국내도서/002외국도서 , pageNumber페이지번호
# https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber=1
for page in range(1, 4):
    url = f"https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber={page}"
    
    # 2) request 이용한 URL 요청
    response = requests.get( url )

    # 3) HTML 파싱
    soup = BeautifulSoup( response.text, "html.parser" )

    # 4) 특정한 마크업 추출( 책 제목, 가격, 저자)
    books = soup.select(".item_info")
    # print(books)

    # 5) 여러개 추출한 마크업에서 특정한 마크업 추출 -> gd.name , yes.b , info_auth
    for book in books :
        title = book.select_one('.gd_name').get_text()
        price = book.select_one('.yes_b').get_text()
        auth = book.select_one('.info_auth').get_text().strip().replace("\n","").replace("\r","")
    
        # 6) 리스트에 담기
        book_list.append({ "제목" :title,"가격":price,"저자" : auth })
print(book_list)