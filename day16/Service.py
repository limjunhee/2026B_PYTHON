# 비지니스 로직 == 머신러닝 모델 예측
import pandas as pd

class ItemService :
    # 생성자
    def __init__(self):
        # self.변수명 = 값 -> 멤버변수 선언
        self.df = pd.DataFrame([
            {'id':1, 'name':'콜라', 'price':1000},
            {'id':2, 'name':'사이다', 'price':1500}
        ])

    def items( self ):
        # df.to_dict( orient = "records")
        # 행 마다 딕셔너리 변환하여 리스트 반환 함수
        return self.df.to_dict( orient="records" )
##############################################################################
# 서비스 객체 생성
item_service = ItemService()