class A(object): # 괄호 안에 object는 파이선에서는 없어도 된다.
    def __init__(self):
        self.aa = 10
    def printA(self):
        print(self.aa)

class B(A): # A 크래스를 상속받음
    def __init__(self):
        super().__init__() # A.__init__(self)     #super(B, self).__init__()
        self.bb = 20
    def printB(self):
        print(self.bb)

class C(B):
    def __init__(self):
        super().__init__()  #B.__init(self)      #super(C, self).__init__()
        self.cc = 20
    def printC(self):
        print(self.cc)
