class Person:
    def __init__(self):
        print('Person__init__')
        self.hello = '안녕하세요.'

class Student(Person):
    pass # 파생 클래스에 생성자(__init__) 가 없다면 자식 클래스는 부모클래스를 그대로 상속받아 사용하게 된다.

james = Student()
print(james.hello)