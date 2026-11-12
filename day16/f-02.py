# 1) import
from fastapi import FastAPI
import uvicorn

# 2) FastAPI 객체 
app = FastAPI()

# 3) uvicorn 서버 실행 함수
if __name__ == "__main__":
    uvicorn.run("f-02:app", host="127.0.0.1", port=8080, reload=True)

# 4) 서버 실행, 현재 파일py 실행 (여러 번 실행 불가)

# 5) HTTP REST 구현, REST: 자원을 주고 받는 상태 구조, REST API: HTTP로 구현한 REST
@app.get("/")
async def index() : #async def 함수명() : 비동기 함수 선언
    return "안녕 파이썬 웹" # 반환값
# 코드 작성 후 서버 재실행 없이 "reload=True" 속성으로 자동 서버 반영

# 2) 쿼리스트링 : HTTP URL 경로 상에 ? 뒤로 정의도니 변수들
@app.get("/user")
async def user( name, age:int ) : # 파이썬은 동적 타입이지만 "변수명:타입명" 정적 타입 기능
    info = {'name' : name, 'age':age, 'msg':'*쿼리통신 성공*'}
    return info # 딕셔너리가 JSON 타입으로 자동 반환

# http://127.0.0.1:8080/doc 접속 후 이름과 나이 넣고 
# Request URL 들어가서 값 제대로 나오는지 확인하기


# 3) 경로 파라미터 : HTTP URL 경로 상에 / 구분하여 변수들
@app.get("/item/{name}/{age}") # item/임준희/25 -> "/item/{변수명}/{변수명}"
async def item( name:str, age:int | None = None) :
    return {name : name, age : age, 'msg' : '경로 통신 성공'}

# http://127.0.0.1:8080/docs?'name'=임준희&'age'=25
# Talend API tester에서 확인 가능

# 4) 본문, HTTP GET/DELETE -> 쿼리/경로, HTTP POST/PUT -> 쿼리/경로/본문BODY
@app.post("/products")
async def products( product:dict ) : # 전달받은 body본문(json) 값을 파이썬 dict 타입으로 매핑
    product['msg'] = "*본문통신성공*"
    return product

# http://127.0.0.1:8080/doc 접속 후 /products 부분에서 body에
# 임의의 딕셔너리 넣어보고 실행해보기
# {
#   "name": "임준희",
#   "age":"25"
# }

