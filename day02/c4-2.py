# p.216 딕셔너리

# 리스트 : 인덱스를 기반으로 값을 저장
# 딕셔너리 : 키(key)를 기반으로 값을 저장

# 중괄호{}로 선언, {key: value} 형태를 쉼표로 연결하여 만듬 -> { key: value, key: value }
# 키로는 문자열, 숫자, 불 등으로 선언 가능하나 일반적으론 문자열로 선언
# JS:JSON, JAVA:MAP/DTO, DB:RECORD

# 1. 선언
dict_a = {'name' : '어벤저스 엔드게임', 'type':'히어로 무비'}

# 2. 값 호출 -> 딕셔너리명['키']
print( dict_a['name'] ) # 어벤저스 엔드게임
print( dict_a['type'] ) # 히어로 무비
# print(dict_a.name) # AttributeError

# 3. 속성값추가 -> 딕셔너리명[새로운키] = 새로운 값
dict_a['price'] = 5000
print(dict_a)   # {'name': '어벤저스 엔드게임', 'type': '히어로 무비', 'price': 5000}

# 4. 속성값 수정
dict_a['type'] = '호러 무비' # 이미 존재하는 키에 값을 넣으면 값이 수정됨
print(dict_a)   # {'name': '어벤저스 엔드게임', 'type': '호러 무비', 'price': 5000}

# 5. 속성값 삭제 -> del 딕셔너리명['key']
del dict_a['price']
print(dict_a)   # {'name': '어벤저스 엔드게임', 'type': '호러 무비'}

# 6. 딕셔너리 내부 키 존재여부 확인 -> '찾을키' in 딕셔너리명
print( 'price' in dict_a ) # False
print( 'type' in dict_a )  # True

# 7. 속성값 호출 방법 1: 딕셔너리명['key'] , 방법2: 딕셔너리명.get(key)
# 차이점 : 방법1은 존재하지 않으면 예외가 발생, 방법 2는 존재하지 않으면 None 반환
print(dict_a.get("name")) # 어벤저스 엔드게임
print(dict_a.get("price")) # None


# 8. 딕셔너리 반복문, 딕셔너리 내 key를 순회한다.

for key in dict_a :
    print( dict_a.get(key) )
    print( dict_a["key"] )

'''
    name : 어벤저스 엔드게임
    type : 호러 무비
'''