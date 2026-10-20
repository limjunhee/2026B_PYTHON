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
list_c + [3]        # 방법 1 [ 1,2,3 ] 새로운 리스트를 생성, 파괴적인 방식
list_c.append(3)    # 방법 2 [ 1,2,3 ] 기존 리스트를 유지함, 비파괴적인 방식