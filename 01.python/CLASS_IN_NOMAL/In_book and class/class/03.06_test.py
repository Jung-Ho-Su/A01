class Person:
    def greeting(self):
        print("안녕하세요.")

class Student(Person): # 상속할 때 괄호 안에 상속 받을 클래스를 기술하면 되고
    # 2개 이상의 클래스도 상속이 가능 하다 이런 것을 다중 상속이라고 한다.
    # 현재는 단일 상속이지만 파이선은 다중 상속이 가능한 언어이다.
    #클래스에 속해있는 함수는 하나지만 상속을 받아서 2개의 함수를 시행할 수 있게 된다
    def study(self):
        print("공부하기")

james = Student()
james.greeting()   # 안녕하세요. : 기반 클래스 Person의 매서드 호출
james.study()      # 공부하기 : 파생 클래스 student에 추가한 study 매서드