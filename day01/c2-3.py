# p.115 변수
pi = 3.14159265 # 변수명 = 값
r = 10            # 변수명 = 값
# r2                 # 초기값 없으면 NameError

print(pi, r) # 변수를 참조함
print(2 * pi * r ) # 62.831853

# p.116 복합 대입 연산자
number = 100
number += 10    # 110
number -= 10    # 100
number *= 2     # 200
number /= 2     # 100.0
number %= 3     # 0.0
print(number)   # 1.0

number = "안녕하세요"
number += "!"
print(number) # 안녕하세요!
number *= 3
print(number) # 안녕하세요!안녕하세요!안녕하세요!

# p. 118 사용자에게 입력받기 -> input("프롬프트문자열")
# 반환 타입 문자열(str)
input("인사말을 입력하세요!> ")

string = input("입력> ")    # 입력받은 값을 변수에 저장하기
print(type(string))         # 입력받은 값의 타입을 확인하기 <class 'str'>


# p.121 타입 변환 str -> int or float / int or float -> str
string_int = int(string)
string_float = float(string)
print(type(string_int), type(string_float))

string_str1 = type(string_int)
string_str2 = type(string_float)
print(type(string_str1), type(string_str2))
# 주의 : 'a3' -> 숫자로 변환 X
# 소수점 있는 문자열은 int로 변환할 수 없음에 주의


# p.125 누적예제
user_input = input("숫자를 입력하세요(단위:inch)>")
inch = int(user_input)
cm = inch * 2.54

print(inch,"인치를 센티미터 단위로 변환하면", cm,"센티미터입니다.")