# 상속이란? 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 것
# isintance( 인스턴스, 클래스명 ) -> 해당 클래스가 어떤 클래스를 기반으로 속성과 기능을 받았는지 확인하는 함수
# 예1
class Student :
    def __init__(self):
        pass

class Human :
    def __init__(self):
        pass

student = Student()

print( isinstance(student, Student) ) # True
print( isinstance(student, Human) ) # False

# p.478
class Student1 :

    # p.484 클래스 변수 : 인스턴스 없이 사용 가능한 변수 (Static, 정적임)
    # 클래스변수명 = 초기값
    count = 0
    students = [ ]

    # p.486 클래스함수
    @classmethod #클래스 함수 정의하는 데코레이터(= 어노테이션)
    def print(cls) : # 매개변수에 cls 관례적으로 선언함
        for student in cls.students : # cls.클래스변수 <-- 동일 --> Student2.클래스변수
            print( str( student ) ) 


    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student1.count += 1 # 클래스변수 호출 방법: 클래스명.변수명
        Student1.students.append(self)

    def get_sum( self ) :
        return self.korean + self.math + self.english + self.science
    
    def get_average(self) :
        return self.get_sum() / 4
    
    def to_string( self ) :
        return "{} \t {} \t {}".format(self.name, self.get_sum(), self.get_average())

    # 특수한 이름의 메소드 (오버라이딩)
    def __str__(self):
        return "{} \t {} \t {}".format(self.name, self.get_sum(), self.get_average())

    # 총 합계 비교 함수 재정의(오버라이딩)
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()  # 같다
    def __ne__(self, value):
        return self.get_sum() != value.get_sum() # 다르다
    def __gt__(self, value):
        return self.get_sum() > value.get_sum() # 크다
    def __ge__(self,value):
        return self.get_sum() >= value.get_sum() # 크거나 같다
    def __lt__(self,value):
        return self.get_sum() < value.get_sum() # 작다
    def __le__(self,value):
        return self.get_sum() <= value.get_sum() # 작거나 같다

students = [
    Student1("윤인성", 87, 98, 88, 95),
    Student1("윤인성", 87, 98, 88, 95),
    Student1("윤인성", 87, 98, 88, 95),
    Student1("윤인성", 87, 98, 88, 95),
    Student1("윤인성", 87, 98, 88, 95),
    Student1("윤인성", 87, 98, 88, 95)
]

# 특수한 이름의 메소드 호출
# str(인스턴스) vs str()
# __str__을 재정의하지 않으면, 주소값 또는 문자열을 변환
print( str(students[0]) ) # __str__ 함수 실행된다 -> 윤인성 358 89.5

# __eq__를 Student1에 오버라이딩 했기 때문에 주소값이 아니라 값을 비교하는 기능이 동작된다. 
# = 서로 다른 객체이지만 총 합계는 같다.
print(students[0] == students[1]) # True, == 대신에 __eq__가 실행된다.

# 원래 객체는 다르지만, __ne__ 메소드에서 주소값이 아닌 총합계를 비교하도록 재정의했다.
print(students[0] != students[1]) # False

# 클래스 변수 호출
print(Student1.count) # 6 출력, __init__가 6번 출력돼서 6임

Student1.print()



# p.491 프라이빗 변수
class Circle:
    def __init__(self, radius):
        self.__radius = radius # java: private int radius
        self.__radius2 = radius # 프라이빗변수

    def get_circumference( self ):
        return 2*self.__radius # 클래스 내부에서 프라이빗 변수 사용 가능
    #getter and setter
    def get_radius(self):
        return self.__radius # 프라이빗 변수 반환하는 getter 함수
    def set_radius(self, radius):
        self.__radius = radius # 매개변수값을 프라이빗 변수에 저장하는 setter 함수
    
    @property # getter (자동생성)
    def radius2( self ):
        return self.__radius2
    
    @radius2.setter # setter (자동생성)
    def radius2( self, value ) :
        self.__radius2 = value

circle = Circle( 10 )
# print( circle.__radius ) # 오류 - private라 안됨 ( AttributeError: 'Circle' object has no attribute '__radius' )
print( circle.radius2 ) # 10

print( circle.get_radius()) # 10
circle.set_radius(20)
print( circle.get_radius()) # 20
print(circle.radius2)       # 10
circle.radius2 = 20
print(circle.radius2)       # 20


# p.497 상속 활용
class Parent :
    def __init__(self):
        self.value = "테스트"
        print( "init 메소드 호출" )
    def test( self ) :
        print( "test()메소드 호출")

# 파이썬은 부모 클래스 여러 개 지정 가능. 
# 부모 클래스끼리 똑같은 이름의 메서드를 가질 경우 super() 대신 부모클래스명().메소드() 로 작성해야 한다.
# class 자식클래스명(부모클래스명1, 부모클래스명2, ...) : 
class Child( Parent ) : #JAVA : class 자식클래스명 extends 부모클래스명{ }
    def __init__(self):
        super().__init__()      # super().메소드 : 상위 부모 클래스를 가리킴
        print("child의 __init__ 메소드 호출")

    # 이 부분이 있다면, test()를 호출할 때 자식의 test를 호출함(오버라이딩)
    def test(self):
        print('child init 메소드 호출')


child = Child() # 부모의 init, 자식의 init 호출 -> 자식이 만들어질 때 부모도 같이 만들어짐
child.test() # 부모의 test 호출

parent = Parent()
parent.test() # 부모의 test 호출

parent2 = child
parent2.test() # 자식의 test 호출