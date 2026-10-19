# p.135 "문자열".format(값)
string_a = "age:{}".format(10)
print( string_a ) # age:10

string_b = "{} {} {}".format(1,"안녕",True)
print(string_b)
# 주의 : 중괄호, 값의 개수는 일치해야 한다. 일치하지 않으면 IndexError 발생.


# p.137 ~ p.140 생략



# p.141 대소문자 변환
a = "Hello"
print( a.upper() ) # HELLO
print( a.lower() ) # hello



# p.142 양쪽 여백/공백 제거하기(전처리/크롤링 할때 사용)
a = " hello python world     "
print(a.strip()) # 띄어쓰기 아니고 양쪽 끝 여백 제거 -> "hello python world"


# p.143 isOOO 구성을 확인하는 용도의 함수 (반환값 -> boolean)
print("hello".isalpha()) # 알파벳으로 이루어져 있는가? -> True
print("hello".isdigit()) # 숫자인가? -> False


# p.144 문자열 찾기