# 상속이란? 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 것
# isintance( 인스턴스, 클래스명 )
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