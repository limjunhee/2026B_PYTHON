# 파이썬 파일 분리
# AppStart.py  : FastAPI 실행 파일
# Controller.py : http rest 매핑하는 곳
# Service.py    : 로직 파일 (모델 로드 / 예측)
# ※ 실행 전에 train.py 먼저 실행해서 .pkl 파일 만들어둘 것

# 1) 서버 실행
from fastapi import FastAPI
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("AppStart:app", host="127.0.0.1", port=8080, reload=True)

# 2) 컨트롤러에 라우터 연결
import Controller # import 파일명 -> (./Practice_day16/Controller.py)
app.include_router( Controller.router )

# 3) 메인 화면(index.html) 반환
# FileResponse : 파일을 그대로 응답으로 보내주는 기능
# 같은 서버(8080)에서 html 을 열어야 axios 요청이 막히지 않음
from fastapi.responses import FileResponse
@app.get("/")
async def index():
    return FileResponse("./Practice_day16/index.html")

# http://127.0.0.1:8080 접속
