class A:
    def greeting(self):
        print("안녕하세요 A 입니다.")

class B(A):
    def greeting(self):
        print("안녕하세요 B 입니다.")

class C(A):
    def greeting(self):
        print("안녕하세요 C입니다.")

class D(B, C):
    pass

x = D()
x.greeting()
