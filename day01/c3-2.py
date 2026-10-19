# if 조건문
if True : # 출력됨
    print("True입니다.")
    print("ㄹㅇ True입니다.")

if False : # 출력 안됨
    print("얘는 False입니다.")
    print("얘는 출력 안됩니다.")

if 3>5 : # if~else문 -> 5가 3보다 큽니다. 출력
    print("3은 5보다 큽니다.")
else : 
    print("5가 3보다 큽니다.")

point = 90
if point >= 90 : # if~ elif~ elif~ else
    print("A등급")
elif point >= 80 :
    print("B등급")
elif point >= 70 :
    print("C등급")
else :
    print("탈락")

#if중첩
x = 10
if x > 5 :
    if x > 10:
        print("x는 5보다도 크고 10보다도 큽니다.")
    print("x는 5보다 큽니다.")
else :
    print("x는 5보다 작습니다.")

# None, 0, 0.0, 빈 컨테이너(리스트, 문자열, 튜플, 딕셔너리 등)
if 0 :
    print("false인가?")
if 1:
    print("true인가?")


num = float(input("숫자 입력>"))
print(num % 2)

print(4/3)
