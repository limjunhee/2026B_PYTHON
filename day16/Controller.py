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