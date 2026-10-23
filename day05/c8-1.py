# p.460 클래스
'''

    객체란 : 프로그램의 동작을 위해 데이터(상태)와 그 데이터를 다루는 동작(메서드)를 하나로 묶은 실체로,
             다른 객체들과 서로 상호작용하며 프로그램의 기능을 수행하는 단위

             여러 가지 속성을 가질 수 있는 대상, 또는 속성을 가질 수 있는 모든 것

             [리스트]와 {딕셔너리} 역시 객체이다.

    절차지향 프로그래밍 : 데이터를 순서대로 처리하고, 하향식 순차 실행 흐름 -> C (클래스 아니고 구조체)
    객체지향 프로그래밍 : 객체들의 상호작용으로 프로그래밍 설계 -> JAVA/PYTHON/JS
    관점지향 프로그래밍 : 공통되는 기능(로그/검증/보안 등)들을 분리하여 프로그래밍 설계 -> SPRING

    추상화 : 핵심적 기능, 기능을 간추려 내는 것

    클래스 : 객체(인스턴스)를 만들기 전에 객체들의 기능과 속성값들을 미리 설계해둔 설계도와 같은 구조

    인스턴스와 객체의 차이 : 
    객체는 세상에 존재하는 모든 데이터들을 추상화한 것(실체 X) -> 개념적인 객체
    인스턴스는 어떤 클래스로 만든 실제 객체(실체 O) -> 물리적 객체

    인스턴스화 : 컴퓨터 안의 객체 정보를 저장 ( JAVA에선 new 생성자() , PYTHON에선 생성자() )

    생성자 : 클래스를 기반으로 실제로 객체를 생성하는 (객체를 초기화하는) 함수

'''


# 1. 클래스 만들기
class Student :
    pass

# 2. 생성자 - 클래스이름() (클래스 이름과 다르면 일반 함수가 된다. = 클래스 호출이 아님)
student = Student(); # new Student() -> X 이건 JAVA의 방식

students = [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student()
]

# p.467
# 2. 생성자
class Student2 :
    
    # def __init__(self, 멤버변수1, 멤버변수2, 멤버변수3):
    #     self.멤버변수1 = 멤버변수1;
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    # def 메소드명( self, 매개변수1 ) :
    def get_sum( self ) :
        return self.korean + self.math + self.english + self.science
    
    def get_average(self) :
        return self.get_sum() / 4
    
    def to_string( self ) :
        return "{} \t {} \t {}".format(self.name, self.get_sum(), self.get_average())


# 일반 함수와 메소드 차이
# 일반 함수는 클래스 밖에서 독립 선언, self가 없음
# 메소드는 클래스 안에서 선언, self를 사용
def get_sum2() :
    pass


# 생성자 이용한 인스턴스 생성 -> 클래스명( 인수, 인수, 인수 )
# JAVA : Student2 s = new Student("유재석", 10, 20, 30, 40)
students = [
    Student2("윤인성", 87, 98, 88, 95),
    Student2("윤인성", 87, 98, 88, 95),
    Student2("윤인성", 87, 98, 88, 95),
    Student2("윤인성", 87, 98, 88, 95),
    Student2("윤인성", 87, 98, 88, 95),
    Student2("윤인성", 87, 98, 88, 95),
    Student2("윤인성", 87, 98, 88, 95)
]


# 인스턴스 내 멤버변수 호출
print( students[0].korean )

print( "이름", "총점", "평균", sep="\t")
for student in students :
    print(student.to_string())


'''
    a.b - 멤버변수
    A.B - 전역변수(Static)
    a.b() - 메소드/함수
    A.b() - 메소드/함수(Static)
'''