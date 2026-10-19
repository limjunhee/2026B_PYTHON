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


# p.144 문자열 찾기 find(), IndexOf()
output_a = "안녕안녕하세요".find('안녕')
print(output_a) # 0

output_b = "안녕안녕하세요".rfind('안녕')
print(output_b) # 2

output_c = "안녕안녕하세요".rfind('hello')
print(output_c) # -1 -> (없다)

# p.145 찾을값 in "문자열", 반환값은 boolean
print("안녕" in "안녕하세요") # True
print("hello" in "안녕하세요") # False

# p.145 "문자열".split("기준문자")
a = "10 20 30 40 50".split(" ") # 공백/띄어쓰기 기준으로 잘라서 list로 반환
print(a) # ['10', '20', '30', '40', '50']
print(a[2]) # 30

# p.146 f-문자열
num = 10
a1 = "age:{}".format(num)   # 숫자10, 변수호출 가능
a2 = f"age:{num}"           # 숫자10, 변수호출 가능
a3 = "age:num+1"            # 문자열10, 변수호출 X
print(a1, a2, a3)           # age:10 age:10 age:num+1