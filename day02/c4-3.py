#p.231 범위 자료형 range()

# 1. range(a) -> 0부터 a-1까지 정수로 된 범위
print(range(5)) #range(0, 5)
print(list(range(5))) # [0, 1, 2, 3, 4]

# 2. range(시작값, 끝값)
print( list(range(3,6))) # 3 ~ 5 -> [3, 4, 5]

# 3. range(시작값, 끝값, 증감단계)
print(list(range(0, 10, 2))) #0부터 9까지 2씩 증가 -> [0, 2, 4, 6, 8]


# p.233
# for range 함수 함께 사용 -> for i in range(10) :
# 1. 1부터 10까지 출력하기
for i in range(1,11) :
    print(i)

# 2. 10부터 1까지 출력하기
for i in range(10, 0, -1) :
    print(i)

# 3. 1~10 중 홀수만 출력하기
for i in range(1, 11, 2) :
    print(i)

# 4. 구구단 : 단수 2부터 9단까지, 곱수 1부터 9까지
for i in range(2,10):
    for j in range(1,10):
        print(i*j)


# p.240 while문

# 1. 1부터 10까지 출력해보기
i = 1
while i <= 10 :
    print(i)
    i += 1

# p.242 while 반복문 : 상태를 기반으로 반복하기
list_a = [1,2,1,2]
value = 2

while value in list_a:
    list_a.remove(value)

print(list_a)

# p.244 break/continue
# break : 반복문을 종료해버림
# continue : 현재 반복단계를 즉시 끝마치고 다음 반복으로
for i in range(1,11,1):
    if i == 3 :
        break
    print(i)
for i in range(1,11,1) :
    if i == 3 :
        continue
    print(i)



# 확인문제 1
for i in range(3,10,3):
    print(i)

# 확인문제 2
key_list = ["name", "hp","mp","level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(0, len(key_list)) :
    character[key_list[i]] = value_list[i]

print(character)

# 확인문제 3
limit = 10000
i = 1

sum_value = 0
while sum_value <= 10000:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며, 그때의 값은 {}입니다.".format(i-1, limit, sum_value))


# 확인문제 4
max_value = 0
a = 0
b = 0

for i in range(1, 101):
    j = 100 - i

    if i * j > max_value :
        max_value = i*j
        a = i
        b = j

print(f"최대가 되는 경우는 {a}*{b}={max_value}이다.")