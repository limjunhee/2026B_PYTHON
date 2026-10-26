# p.250 문자열, 리스트, 딕셔너리와 관련된 기본 함수

# p.251
numbers = [103, 52, 273, 32, 77]
print(min(numbers)) # 32 : 리스트의 최솟값
print(max(numbers)) # 273 : 리스트의 최댓값
print(sum(numbers)) # 537 : 리스트 안 요소값들의 총합


# p.252 reversed(리스트)
numbers_reversed = reversed(numbers) # 리스트 뒤집기
print( list(numbers_reversed ) ) # 리스트 타입으로 변환하여 출력 -> [77, 32, 273, 52, 103]

print(numbers_reversed) # <list_reverseiterator object at 0x0000025B69D24EE0> -> 이터레이터 출력
next(numbers_reversed)
# 이터러블 : 리스트, 딕셔너리처럼 내부의 요소들을 차례차례 꺼낼 수 있는 객체를 의미
# 이터레이터 : 이터러블 중에서 하나씩 차례로 빼낼 수 있는 요소
# 이터레이터 가능한 타입 : 리스트, 딕셔너리, 문자열, 튜플 등
# 이터레이터 하나씩 꺼내는 함수 -> next() 함수 --------------> 이터러블


# p.254 enumerate()
numbers = [103, 52, 273, 32, 77]
print(numbers) # [103, 52, 273, 32, 77]
print(enumerate(numbers)) # <enumerate object at 0x0000025B6C377A10>
print(list(enumerate(numbers))) # (인덱스, 값) 튜플들의 리스트로 반환 -> [(0, 103), (1, 52), (2, 273), (3, 32), (4, 77)]
for index, value in enumerate(numbers) :
    print(index, value)
    '''
    0 103
    1 52
    2 273
    3 32
    4 77
    '''

# p.256 딕셔너리.items(), [ (key, value), (key, value)]
dict_a = {"name": "유재석", "age":10}
for key, value in dict_a.items() :
    print(key, value)
    '''
    name 유재석
    age 10
    '''

# p. 258 리스트 내포 , 인덱스 자리에 반복문 사용 가능
# 0부터 20까지 2씩 증가한 자료들을 리스트에 저장

# 방법 1
array = []
for i in range(0, 21, 2) :
    array.append(i)

# 방법 2 리스트변수 = [ 값 for 반복변수 in range() ]
array = [i for i in range(0,21,2)] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(array)

# 방법 3 리스트변수에 조건 추가 [ 값 for 반복변수 in range() if 조건식]
array = [i for i in range(0,21,2) if i != 10] # [0, 2, 4, 6, 8, 12, 14, 16, 18, 20]
print(array)


# p.263 join() 함수
# 방법 1 '''여러줄'''
print('''안녕하세요1
안녕하세요2''')

# 방법 2 \n 제어문자
print("안녕하세요1\n안녕하세요2")

# 방법 3 ("문자열" "문자열" "문자열") -> 투플 사용
print(("안녕하세요1\n" "안녕하세요2"))

# 방법 4 join() 함수 -> 사이에 넣을 문자.join(문자열리스트) = 리스트 요소 사이마다 특정 문자열을 삽입
print("\n".join( ["안녕하세요1", "안녕하세요2"] )) # 안녕하세요1\n안녕하세요2
print("\n".join( "안녕하세요1")) # 안\n녕\n하\n세\n요\n1
print("-".join("유재석")) # 유-재-석


# 확인문제 2
output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]

for i in output :
    print("{} : {}".format(i, "{:b}".format(i)))

print("합계:", sum(output))