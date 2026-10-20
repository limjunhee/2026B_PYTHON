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
print(list_a[1][1]) # TypeError 발생 -> 숫자형은 문자열 취급 X, 하나의 리터럴 취급