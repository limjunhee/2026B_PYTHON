# p.192
# 리스트 -> [1, 2, 3, 4, 5]
# 요소(element)
# 인덱스(index) -> 리스트 내 요소들이 저장된 순서 번호, 0번부터 시작

list_a = [ 274, 43, 321, "문자열", True, False ] # 리스트 선언
print(list_a[2])
print(list_a[1:3]) # 슬라이싱 : 1번 인덱스부터 2개 -> [43, 321]

list_a[2] = 7
print(list_a)

print(list_a[2])  # 인덱싱
print(list_a[-2]) # 음수 인덱싱

print(list_a[3][1]) # '자' 출력 -> 문자열도 리스트이기 때문에 가능
# print(list_a[1][1]) # TypeError 발생 -> 숫자형은 문자열 취급 X, 하나의 리터럴 취급

list_1 = [1, 2, 3] # 1차원 리스트
list_2 = [
    [1,2], 
    [3,4], 
    [5,6] ] # 2차원 리스트, 표의 [행][열] 순으로 보면 이해하기 쉽다. pandas 등을 사용하면 더 편해짐
print(list_2[1][0]) # 3 출력

# print(list_2[4][5]) # IndexError: list index out of range


# 리스트 연산 -> 연결(+), 반복(*), len()
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print(list_a + list_b)  # [1, 2, 3, 4, 5, 6]
print(list_a * 3)       # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(list_a))      # 3

list_aa = [[1],[2],[3]]
print(list_a + list_aa) # [1, 2, 3, [1], [2], [3]]

list_a.append( 4 )
print(list_a)           # [1, 2, 3, 4]
list_a.insert(0, 5)     # 특정 인덱스에 새로운 요소 삽입 (0번 인덱스에 5 삽입)
print( list_a )         # [5, 1, 2, 3, 4]

# 주의할 점:
list_c = [1,2]
list_c + [3]        # 방법 1 [ 1,2,3 ] 새로운 리스트를 생성, 파괴적인 방식 = .extend(3)
list_c.append(3)    # 방법 2 [ 1,2,3 ] 기존 리스트를 유지함, 비파괴적인 방식


# p.202 리스트 요소 제거하기
list_a = [1, 2, 3, 4, 5]

# del 리스트명[인덱스]
del list_a[1] # 1번 인덱스 삭제
print(list_a) # [1, 3, 4, 5]


# 리스트명.pop(인덱스값)
list_a.pop( 2 ) # 2번 인덱스 삭제 -> 4 삭제
print(list_a)   # [1, 3, 5]

del list_a[0:2] # del 키워드 이용한 슬라이싱 삭제
print(list_a) # [5]

# 리스트명.remove(요소 값)
list_a.remove( 5 )  # 요소값 5번이 있다면 삭제
# list_a.remove(1)    # 값이 없을 경우 ValueError 발생
print(list_a)       # []


# 리스트명.clear
list_a.clear() # 전체 삭제

# 리스트 슬라이싱 -> 인덱스명[시작인덱스:끝인덱스:증감단계]
nums = [1,2,3,4,5,6,7,8,9]
print(nums[0:5:2])      # [1, 3, 5] -> 0번부터 5번까지 2단계 뛰면서 세라
print(nums[::-1])       # [9, 8, 7, 6, 5, 4, 3, 2, 1] -> 맨 뒤부터 앞까지 하나도 빠짐없이 세라

# p.205 정렬 -> 리스트명.sort() , 리스트명.sort(reverse=True)
list_e = [52, 27, 103, 32, 275, 1, 5]
list_e.sort()
print(list_e) # [1, 5, 27, 32, 52, 103, 275]
list_e.sort(reverse=True)
print(list_e) # [275, 103, 52, 32, 27, 5, 1]

# p.206 내부 확인, 찾을값 in 리스트
print( 52 in list_e ) # True
print( 51 in list_e ) # False
print( 52 not in list_e ) # True -> False
print( 51 not in list_e ) # False -> True


# p.208 리스트와 반복문 , 리스트 내 요소들이 순차적인 인덱스 구조

# for 반복변수 in 반복가능자료 :
#   실행코드

for element in list_e :
    print( element )

for char in '안녕하세요' : # 문자열도 리터럴(문자)이 모여 형성된 리스트라 반복 가능
    print(char)


# p.211 전개 연산자 *리스트명 -> 리스트명[0], 리스트명[1] ...
# 리스트 요소를 전개하여 입력한 것과 같은 효과를 냄
a = [1,2,3,4]
b = [*a, *a]
print(b) # [1, 2, 3, 4, 1, 2, 3, 4]

c = [*b, 5] # [1, 2, 3, 4, 1, 2, 3, 4, 5]
print(c)