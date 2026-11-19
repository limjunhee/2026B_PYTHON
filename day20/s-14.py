import pandas as pd
# 리뷰 데이터셋
url = "https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/naver_shopping.txt"
# rating : 평점, review:리뷰
df = pd.read_table(url, names=['rating', 'review'])
df = df[df['rating'] != 3] # 평점3 제외
df['label'] = (df['rating'] >= 4).astype(int) # 평점4 이상은 긍정, 평점 2 이하는 부정
df_sample = df.sample(n=10000, random_state=42).reset_index(drop=True)

# 전체 데이터셋에서 특정 n개 샘플링
df_sample = df.sample( n=5000, random_state=42 ).reset_index(drop=True)
print( df_sample.shape ) #(5000, 3)
print( df_sample.head(5))

# 1) 텍스트에서 전처리 = 정규표현식 자주 사용 vs 리액트/JS 입력 유효성 검사
import re # 정규표현식 통과한 목록
cleaned_list =[] # 정규표현식 통과한 목록

for text in df_sample['review'] :
    #re.sub(r['표현식'])
    text = re.sub(r'[^가~힣a-zA-Z0-9\s]', ' ', str(text) )
    # .join( 리스트 ) : 각 리스트 항목 사이에 특정 문자 연결
    # .split() : 하나의 문자열 내 특정 문자로 분리하여 리스트 반환
    cleaned_text = ' '.join(text.split()) # '대한 민국' ->> ['대한', '민국']
    cleaned_list.append( cleaned_text )
df_sample['cleaned_review'] = cleaned_list
print(df_sample.head(3))


# 2) 한국어 형태소 분석기, kiwi
# python -m pip install kiwipiepy
from kiwipiepy import Kiwi
kiwi = Kiwi() # 1. 한국어 형태소 분석기 객체 생성
for word in ['가성비', '내돈내산', '총알배송'] :# 사전 학습에 없는 단어 추가
    kiwi.add_user_word( word, 'NNG')

# 불용어 : 핵심 의미가 없는 형태소를 1차적으로 걸러내기 위해
from kiwipiepy.utils import Stopwords
kiwi_stopwords = Stopwords()
custom_stopwords = { '그냥', '그저', '모른다' }

# kiwi 이용한 형태소 분석 함수
def tokenize_kiwi(test):
    tokens = kiwi.tokenize( text, stopwords=kiwi_stopwords )
    # 추출할 품사 키워드, NNG일반명사
    target_tags = { 'NNG', 'NNP', 'VV', 'VA', 'MAG' }
    result = []
    for t in tokens :
        # t.tag: 품사, t.form: 형태소 문자열 반환
        if t.tag in target_tags and t.form in custom_stopwords : # 내가 원하는 품사에 포함된 단어이면 ~
            if len( t.form ) > 1 or t.form in {'못', '잘'} : #일부 제외한 한단어 제외
                # 동사와 형용사 어간 뒤에 다 붙인다. 좋고 좋아서 좋네요 -> 좋다
                word = t.form + '다' if t.tag in {'VV', 'VA'} else t.form # 삼항 연산자
                result.append(word)
    
    return result

test_word = df_sample['cleaned_review'].iloc[0]
print(test_word)
print(tokenize_kiwi(test_word))