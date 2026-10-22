# 예외 객체 : 발생한 예외 정보를 갖는 객체
# 예외 클래스 : Exception(예외 최상위클래스)
# Exception as 변수명 : 
# as 키워드 : 클래스의 객체변수
# 그 외 모든 예외 처리 : 여러 개 except에서 Exception은 항상 마지막에 위치할 것
# 주의 : Exception이 앞에 위치해버리면 아래 except 예외가 작동하지 않음
# raise : 강제로 예외 발생, 주로 CRUD 실패 의미(500)
# p.383
list_number = [ 52, 273, 32, 72, 100 ]
try: 
    number_input = int( input('정수입력: ')) # 타입 예외 발생 가능
    print( list_number[ number_input ])     # 인덱스 예외 발생 가능
    raise NotImplementedError
    # java에선 throws new 예외클래스()
except ValueError as e : # invalid literal for int() with base 10: 'a' -> 타입변환 예외
    print( e )
except IndexError as e : # list index out of range -> 인덱스 예외
    print( e )
except Exception as e : # 그 외(최상위) 예외 -> 항상 마지막에 배치
    print( e )


# p.350 스택과 힙을 알고 global 키워드 사용하기
a = 10
def 함수() :
    # 단순 전역변수 호출이면 global 생략 가능
    # 전역변수 수정하면 global이 필수
    #print(a) # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    global a
    a = a + 1
    print( a ) # global 없어도 전역스택 가능
    a = 20      # 함수 스택
함수()
