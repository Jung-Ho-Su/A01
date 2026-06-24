class Person:
    def __init__(self, name, age, address, wallet): # __init__ 생성자를 적고 뒤에 ()를 적은 뒤
        # self. ... ... ... 을 적어서 속성을 여러개를 정의해준다.
        self.name = name #  여기서 self 뒤에 다 속성이다.
        self.age = age
        self.address = address
        self.__wallet = wallet #변수 앞에 __를 붙여서 비공개 속성으로 만듦


# 여기서 인스던스 = 클래스()의 형태로 여기서 ()안의 값들은 인스던스(=객체)에 할당해서 들어갈 클래스의 속성에 할당되는 값들이다
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000 # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
