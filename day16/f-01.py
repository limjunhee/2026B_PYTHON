# Fast api : HTTP 비동기 통신 지원하는 프레임워크
# 설치 : python -m pip install fastapi uvicorn

# 1) FastAPI로 uvicorn 서버 실행
from fastapi import FastAPI
import uvicorn

# 2) FastAPI 객체 만들기, 자바: new 클래스() vs 파이썬: 클래스()
app = FastAPI()

# 3) uvicorn 서버 실행 함수만들기, 파이썬 main 함수 만들기
# java에서의 main 함수 -> 메인 스레드 내장 포함하여 프로세스 실행 최초 실행 함수
# 파이썬 if __name__ == "__main__" : 해당 py 실행되면 먼저 진입되는 구역
if __name__ == "__main__":
    uvicorn.run("f-01:app", host="127.0.0.1", port=8080, reload=True)

# 4) 서버 실행 방법 : 현재 uvicorn.run 존재하는 파일에서 py 실행
# http://127.0.0.1:8080
# 5) 서버 종료 방법 : 해당 서버 터미널에서 ctrl+c 또는 터미널 닫기
# 6) 서버 REST API 확인 : 127.0.0.1/docs