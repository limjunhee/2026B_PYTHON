# p.361
# 구문 오류 : 실행 전 오류, 실행 자체가 불가
# 런타임 오류(예외) : 실행 도중 발생하는 오류

# 조건문 또는 try
# 예1) 조건문 예외
input_a = input( "정수 입력> " )
# int_input = int(input_a) # '문자열' 입력 시 ValueError 발생
if input_a.isdigit() : # 문자열.isdigit() : 문자열 타입의 값이 숫자이면 true 반환
    int( input_a )
else :
    print( "정수가 아닙니다." )

# 예2) try 예외
try:
    int( input_a ) # 예외가 발생할 것 같은 코드
except:
    print( "정수가 아닙니다." ) # 예외가 발생할 경우 실행시킬 코드


# p.367 try except + pass 키워드 조합
try :
    int( input_a ) # 예외가 발생할 것 같은 코드
except :
    # except 구문 내부에 아무것도 넣지 않으면 오류 발생
    # pass 키워드로 프로그램 꺼지는 것만 방지.
    pass


# p.369 try except + else 키워드 조합
try :
    int( input_a ) # 예외가 발생할 것 같은 코드
except :
    pass # 예외가 발생했을 때 실행할 코드
else :
    # else를 굳이 쓸 필요는 없지만 다른 사람의 코드에서 발견될 수 있으므로 알아는 두자
    print("정수를 올바르게 입력하셨습니다.") # 예외가 발생하지 않았을 때 실행할 코드


# p.370 finally 키워드 : 예외가 발생하든 말든 무조건 실행시킬 코드
try:
    int(input_a) # 예외가 발생할 만한 코드
except :
    print("정수가 아닙니다.") # 예외 발생 시 실행할 코드
else :
    print("정수가 맞습니다.") # 예외 발생 안할 경우 실행할 코드
finally :
    print("프로그램 종료") # 예외 발생여부 상관 없이 실행할 코드



# p.373 finally 왜 써야 하나 (finally 활용 예시)
try:
    file = open("info.txt", "w") # 파일 불러오기 함수, w옵션 : vkdlf djqtdmaus todtjd
    일부러.예외발생() # 예외 발생 시 이후 코드는 실행 안하고 무시함 -> file.close() 실행 X
    file.close()     # 예외 발생해서 실행 X
except:
    print("오류 발생")

print("파일 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed) # file.closed: False

# ==========================[ finally 쓸 경우 ]=============================
try:
    file = open("info.txt", "w")
    일부러.예외발생()
except:
    print("오류 발생")
finally :
    file.close()

print("파일 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed) # file.closed: True


# 확인문제

#2번
numbers = [52,273,32,103,90,10,275]
print("(1)")
print("- {}는 {}위치에 있음".format(52, numbers.index(52)))
print()

print("2")
number = 10000
if number in numbers:
# try:
    print("- {}는 {}위치에 있음".format(number, numbers.index(number)))
else :
# except:
    print("- 리스트 내부에 없는 값입니다.")
print()

print("--- 정상적으로 종료되었습니다. ---")

# 3번
# a = 10+"ro"
# int("dsad")
# cursor.close)
# [1,2,3,4,5][10]