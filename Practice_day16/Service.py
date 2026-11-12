# 비지니스 로직 == 머신러닝 모델 예측
# 서버 시작할 때 저장된 모델(.pkl) 한 번만 불러옴 -> 요청마다 재학습 X, 예측만 수행
import joblib
import pandas as pd

class BikeService :
    # 생성자 : 모델, 성능 지표 로드
    def __init__(self):
        self.model = joblib.load( './Practice_day16/bike_model.pkl' )
        self.metrics = joblib.load( './Practice_day16/bike_metrics.pkl' )
        self.weekday_names = ['월', '화', '수', '목', '금', '토', '일']

    def predict( self, data ):
        # 1. 입력 딕셔너리 -> 데이터프레임
        # data 예시 : { 'date':'2018-07-12', 'hour':18, 'temp':27, 'humidity':55, 'wind':2,
        #               'rainfall':0, 'snowfall':0, 'holiday':'No Holiday' }
        df = pd.DataFrame( [data] )

        # 2. 날짜 -> 요일 -> 주말 여부 (학습 때랑 똑같이)
        df['date'] = pd.to_datetime( df['date'] )      # 웹에서 '2018-07-12' 형식으로 옴
        df['weekday'] = df['date'].dt.weekday
        df['weekend'] = 0
        df['weekend'] = df['weekend'].mask( df['weekday'] >= 5, 1 )

        # 3. 월 -> 계절 (데이터셋 기준 : 12~2 겨울 / 3~5 봄 / 6~8 여름 / 9~11 가을)
        df['month'] = df['date'].dt.month
        df['season'] = 'Winter'
        df['season'] = df['season'].mask( ( df['month'] >= 3 ) & ( df['month'] <= 5 ), 'Spring' )
        df['season'] = df['season'].mask( ( df['month'] >= 6 ) & ( df['month'] <= 8 ), 'Summer' )
        df['season'] = df['season'].mask( ( df['month'] >= 9 ) & ( df['month'] <= 11 ), 'Autumn' )

        # 4. 비 여부, 눈 여부 (학습 때 만든 파생변수 똑같이)
        df['rain'] = 0
        df['rain'] = df['rain'].mask( df['rainfall'] > 0, 1 )
        df['snow'] = 0
        df['snow'] = df['snow'].mask( df['snowfall'] > 0, 1 )

        # 화면에 보여줄 요일 이름 (아래에서 weekday 열 빠지기 전에 미리 저장)
        weekday_name = self.weekday_names[ int( df['weekday'][0] ) ]

        # 5. 학습 때랑 같은 컬럼, 같은 순서로 맞추기
        df = df[ ['hour', 'temp', 'humidity', 'wind', 'rainfall', 'snowfall', 'season', 'holiday', 'weekend', 'rain', 'snow'] ]

        # 6. 예측 (음수 나오면 0 으로 -> 대여 수가 마이너스일 순 없음)
        pred = self.model.predict( df )[0]
        if pred < 0 :
            pred = 0

        # 7. 예측 결과 + 모델 성능 지표 반환
        return {
            'prediction' : int( round( pred ) ),                         # 예상 대여 수(대)
            'weekday' : weekday_name,                                    # 요일
            'season' : df['season'][0],                                  # 자동 계산된 계절
            'weekend' : int( df['weekend'][0] ),                         # 주말 여부
            'rain' : int( df['rain'][0] ),                               # 비 여부
            'snow' : int( df['snow'][0] ),                               # 눈 여부
            'r2' : self.metrics['r2'],                                   # 테스트 R2 (필수 지표)
            'model_name' : self.metrics['model_name'],                   # 선택된 모델
            'best_params' : self.metrics['best_params']                  # 최적 하이퍼파라미터
        }

    def info( self ):
        # 모델 성능 지표 전체 (비교표 포함)
        return self.metrics

##############################################################################
# 서비스 객체 생성
bike_service = BikeService()
