from abc import *

class StudentBase(metaclass=ABCMeta): # 추상 클래스를 만들고 싶다면 'metaclass=ABCMeta'을 기술해줘야 한다.
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self): # 추상 매서드를 구현하지 않아 student 인스턴스를 만들 수 없음
        pass

class Student(StudentBase):
    def study(self): # study는 오버로딩(재정의) 해줘서 오류가 안나지만 go_to_school은 오버로딩 해주지 않아서 오류가남
        print('공부하기')

    def go_to_school(self):
        print('학교 가기') # 본래는 go_to_school을 오버로딩(재정의)하지 않아 생긴 오류이기에 오버로딩 해줘서 오류를 잡아줌

    def sleep(self):
        print('낮잠 자기')


class Children(StudentBase):
    def study(self): # study는 오버로딩(재정의) 해줘서 오류가 안나지만 go_to_school은 오버로딩 해주지 않아서 오류가남
        print('재미나게 놀기')

    def go_to_school(self):
        print('유치원 가기') # 본래는 go_to_school을 오버로딩(재정의)하지 않아 생긴 오류이기에 오버로딩 해줘서 오류를 잡아줌

    def sleep(self):
        print('낮잠 자기')


james = Student()
james.study()
james.go_to_school()
print('---------------')
obj = Children()
obj.study()
obj.go_to_school()
obj.sleep()
print('---------------')
lst = []
lst.append(obj)
lst.append(james)
for data in lst:
    data.study()
    data.go_to_school()
    print('############')
