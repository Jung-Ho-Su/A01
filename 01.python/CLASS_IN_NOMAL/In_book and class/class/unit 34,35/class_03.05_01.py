#03.05
#unit 34

class person:
    def __init__(self):
        self.hello = "안녕하세요"


    def greeting(self):
        print(self.hello)

# 객채 = 클래스 를 적는 형식으로 클래스를 사용하기 때문에 이와 같은 형식으로 사용한다 이렇게 사용하는 것이 문법이기 때문이다.
james = person()  # 클래스 할당
james.greeting() # 안녕하세요 # 인스던스.매서드() 의 형식으로 클래스에 작성한 매서드를 사용한다.

