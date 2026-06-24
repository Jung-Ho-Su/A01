class Person:
    def __init__(self): # 해당 클래스가 객체를 생성하는 시점에 생성자가 생성
        print('Person__init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self): # 해결방법 : person클래스에 있는 생성자르 호출하는 문장을 넣어주면 해결된다
        super().__init__() # super()로 기반 클래스의 __init__ 매서드 호출
        print('Student__init__')
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.hello)
print(james.school) # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함