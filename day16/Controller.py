# [1] 라우터 : 특정 도메인(주소) 묶어주는 역할
from fastapi import APIRouter
router = APIRouter( prefix="/api" )

# [2] 다양한 Rest API CRUD
# 서비스 객체 불러오기(./day16/Service.py)
from Service import item_service
# 1) 전체 조회
@router.get("/items")
async def items() :
    # 서비스내 함수
    return item_service.items()

# http://127.0.0.1:8080/api/items -> 상품 딕셔너리 확인

# 2) 저장
@router.post("/save")
async def save( item : dict ):
    return item_service.save( item )

# http://127.0.0.1:8080/api/save 에 접속 후
# { "id": 3, "name":"환타", "price":1300 }

# 3) 수정
@router.put("/update")
async def update(item:dict) :
    return item_service.update(item)

# http://127.0.0.1:8080/api/update 에 접속 후
# { "id": 3, "name":"맛있는환타", "price":1400 }