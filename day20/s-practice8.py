# PythonML Practice8: 텍스트 마이닝 및 감성 분석
# 데이터셋: 네이버 영화 리뷰 감성 분석 데이터 (NSMC - Naver Sentiment Movie Corpus)

# import pandas as pd
# url = 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt'
# df = pd.read_table(url) # id:리뷰ID, document:리뷰내용, label:감성라벨(0:부정, 1:긍정)
# df = df.dropna(subset=['document']) # 결측치 제거
# df_sample = df.sample(n=5000, random_state=42).reset_index(drop=True) # 5,000건 무작위 샘플링

# [단계 1] 정규표현식 기반 리뷰 텍스트 정제
# 1. 한글, 영문, 숫자, 공백을 제외한 특수문자 및 이모티콘을 제거하기 위해 re.sub(r'[^가-힣a-zA-Z0-9\s]', ' ', str(text))를 적용하세요.
# 2. 연속된 공백을 단일 공백으로 통일(' '.join(text.split()))하여 정제된 문장을 리스트에 누적한 뒤, df_sample['cleaned_review'] 컬럼으로 추가하세요.

# [단계 2] 한국어 형태소 분석기 설정 및 사용자 정의 토크나이저 구현
# 1. Kiwi() 객체를 생성하고, 영화 리뷰 도메인 특화 신조어(['노잼', '꿀잼', '갓작', '발연기', '인생영화'])를 품사 태그 'NNG'(일반명사)로 add_user_word()를 통해 등록하세요.
# 2. kiwipiepy.utils.Stopwords() 기본 불용어 객체와 영화 리뷰용 추가 불용어 집합({'영화', '진짜', '정말', '그냥', '너무', '완전'})을 정의하세요.
# 3. 일반명사('NNG'), 고유명사('NNP'), 동사('VV'), 형용사('VA'), 일반부사('MAG')만 추출하되, 1글자 형태소는 제외(단, '못', '잘'은 예외 허용)하고 동사/형용사 어간 뒤에 '다'를 결합하여 기본형으로 복원하는 tokenize_kiwi(text) 함수를 작성하세요.

# [단계 3] 학습/테스트 데이터 분할 및 TF-IDF 벡터화
# 1. train_test_split()을 사용하여 특성과 타깃을 8:2 비율로 분할하세요.
# 2. TfidfVectorizer 객체를 생성하여 희소 행렬(X_train_tfidf, X_test_tfidf)을 생성하세요.

# [단계 4] 로지스틱 회귀(LogisticRegression) 기반 감성 분류 모델 학습 및 평가
# 1. LogisticRegression(C=1.0, max_iter=1000, random_state=42) 모델을 생성하고 X_train_tfidf, Y_train 데이터로 fit() 학습을 수행하세요.
# 2. 학습 데이터 정확도(score), 테스트 데이터 정확도(score), 그리고 테스트 데이터 예측값(Y_pred) 기반의 f1_score(Y_test, Y_pred)를 각각 출력하여 모델 성능을 평가하세요.

# [단계 5] 새로운 영화 리뷰 문장 실시간 감성 예측 테스트
# 1. 아래 3개의 새로운 영화 리뷰 문장 리스트(new_reviews)를 정의하고, [단계 1]과 동일한 정규표현식 정제 과정을 적용하여 cleaned_new 리스트를 생성하세요.
#    - "배우들 연기력이 미쳤고 스토리 몰입감이 최고입니다! 무조건 극장에서 보세요."
#    - "시간 아깝고 연출도 엉망이라 중간에 나올 뻔했네요. 최악의 영화입니다."
#    - "킬링타임용으로 나쁘지 않지만 그렇다고 특별히 기억에 남지도 않네요."
# 2. 학습된 tfidf.transform(cleaned_new)로 벡터화한 뒤, model.predict_proba()를 이용해 각 리뷰별 긍정 확률(probs[i][1])과 부정 확률(probs[i][0])을 계산하세요.
# 3. 긍정 확률이 0.4 이상 0.6 이하이면 '중립(애매함)', 0.6 초과이면 '긍정(1)', 0.4 미만이면 '부정(0)'으로 판별하여 리뷰 원문과 함께 예측 결과를 출력하세요.

# =============================================================================================================================================================================================================================================

import pandas as pd
url = 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt'
df = pd.read_table(url) # id:리뷰ID, document:리뷰내용, label:감성라벨(0:부정, 1:긍정)
df = df.dropna(subset=['document']) # 결측치 제거
df_sample = df.sample(n=5000, random_state=42).reset_index(drop=True) # 5,000건 무작위 샘플링

# [단계 1]
import re
cleaned_list = [ ] # 정규 표현식 통과한 목록
for text in df_sample['document'] :
    text = re.sub(r'[^가-힣a-zA-Z0-9\s]', ' ', str(text))
    cleaned_text = ' '.join(text.split())
    cleaned_list.append( cleaned_text )
df_sample['cleaned_review'] = cleaned_list

from kiwipiepy import Kiwi
kiwi = Kiwi()
# 일반명사에 신조어 추가하기
for word in ['노잼', '꿀잼', '갓작', '발연기', '인생영화'] :
    kiwi.add_user_word( word, 'NNG' )

# 불용어 객체 및 집합 정의
from kiwipiepy.utils import Stopwords
kiwi_stopwords = Stopwords()
custom_stopwords = {'영화', '진짜', '정말', '그냥', '너무', '완전'}

# 함수 작성
def tokenize_kiwi( text ) : 
    # kiwi.tokenize( 분석할문장 , stopwords=불용어객체 )
    tokens = kiwi.tokenize( text , stopwords= kiwi_stopwords )
    # 추출할 품사 키워드
    target_tags = { 'NNG' , 'NNP' , 'VV' , 'VA' , 'MAG' }
    result = [ ]
    for t in tokens : # 토큰나이즈가 된 리스트에서 원하는것만 필터링/추출 
        if t.tag in target_tags and t.form not in custom_stopwords: 
            if len( t.form ) > 1 or t.form in { '못' , '잘' } : 
                word = t.form +'다' if t.tag in { 'VV' ,'VA' } else t.form
                result.append(word)
    return result

# [단계 3]
# 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    df_sample['cleaned_review'], df_sample['label'], test_size=0.2,
    random_state=42, stratify=df_sample['label']
)

# TF-IDF 벡터화
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(
    tokenizer=tokenize_kiwi,
    token_pattern=None
)

X_train_tfidf = tfidf.fit_transform( X_train )
X_test_tfidf = tfidf.transform( X_test )


# [단계 4]
# 모델 생성 후 훈련 데이터로 학습
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
model = LogisticRegression( C=1.0, max_iter=1000, random_state=42 )
model.fit(X_train_tfidf, Y_train)

# 학습 데이터 정확도, 테스트 데이터 정확도
print( model.score(X_train_tfidf, Y_train)) # 0.88175
print( model.score(X_test_tfidf, Y_test)) # 0.728

# f1 score
Y_pred = model.predict( X_test_tfidf )
print('f1 :', f1_score(Y_test, Y_pred)) # f1 : 0.7068965517241379


# [단계 5]
new_reviews = [
    "배우들 연기력이 미쳤고 스토리 몰입감이 최고입니다! 무조건 극장에서 보세요.",
    "시간 아깝고 연출도 엉망이라 중간에 나올 뻔했네요. 최악의 영화입니다.",
    "킬링타임용으로 나쁘지 않지만 그렇다고 특별히 기억에 남지도 않네요."
]

# 단계 1과 똑같은 정규표현식
cleaned_new = [ ] # 정규표현식 통과한 목록
for text in new_reviews :
    text = re.sub( r'[^가-힣a-zA-Z0-9\s]',' ', str(text))  
    cleaned_new.append( ' '.join(text.split() ) )

new_tfidf = tfidf.transform( cleaned_new )
probs = model.predict_proba( new_tfidf )

for i in range( len(new_reviews) ) :
    if 0.4 <= probs[i][1] <= 0.6 :
        contents = '중립(애매함)'
    elif probs[i][1] > 0.6 :
        contents = '긍정(1)'
    else :
        contents = '부정(0)'
    print( f'리뷰: {new_reviews[i]}')
    print( f'감성분석: {contents}, 긍정확률: {probs[i][1]}, 부정확률: {probs[i][0]}')

# 리뷰: 배우들 연기력이 미쳤고 스토리 몰입감이 최고입니다! 무조건 극장에서 보세요.
# 감성분석: 긍정(1), 긍정확률: 0.7789363244191427, 부정확률: 0.22106367558085727
# 리뷰: 시간 아깝고 연출도 엉망이라 중간에 나올 뻔했네요. 최악의 영화입니다.
# 감성분석: 부정(0), 긍정확률: 0.08210779006237422, 부정확률: 0.9178922099376258
# 리뷰: 킬링타임용으로 나쁘지 않지만 그렇다고 특별히 기억에 남지도 않네요.
# 감성분석: 부정(0), 긍정확률: 0.3502889319367553, 부정확률: 0.6497110680632447