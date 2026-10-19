# 비교 연산자
# ==, != , < , > , <= , >=

# p.158 범위 논리(파이썬에서만 가능)
x = 25
print(10 < x < 30) # True
print(40 < x < 60) # False

# p.158 not, and , or

# not : 참과 거짓을 반대로 바꿀 때 사용
print(not True) # False
print(not False) # True

# and : 둘 다 참일 때 True 반환
print(True and True) # True
print(True and False) # False

# or : 둘 중 하나라도 참이면 True 반환
print(True or True) # True
print(True or False) # True
print(False or False) # False