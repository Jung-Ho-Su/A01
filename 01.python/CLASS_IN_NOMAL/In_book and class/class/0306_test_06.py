class Person:
    def __init__(self):
        print("Person Class")
    def greeting(self):
        print("안녕하세요.1")

class University:
    def __init__(self):
        print("University Class")
    def manage_credit(self):
        print('학점 관리')
    def greeting(self):
        print("안녕하세요.2") # 앞의 person의 greeting과 이름이 같아서 충돌이 일어나고 여기서 앞에게 사용이된다.

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()