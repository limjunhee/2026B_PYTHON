# 파이썬 파일 분리
# AppStart.py : FastAPI 실행 파일
# Controller.py : http rest 매핑하는 곳
# Service.py : 로직 파일

# 1) 서버 실행
from fastapi import FastAPI
import uvicorn
 
app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("f-02:app", host="127.0.0.1", port=8080, reload=True)