class A: # 괄호 안에 object는 파이선에서는 없어도 된다.
    def __init__(self, x):
        self.aa = x
    def printA(self):
        print(self.aa)

class B(A): # A 클래스를 상속받음
    def __init__(self, x, y):
        super().__init__(x) # A.__init__(self)     #super(B, self).__init__()
        self.bb = y
    def printB(self):
        print(self.bb)

class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)  #B.__init(self)      #super(C, self).__init__()
        self.cc = z
    def printC(self):
        print(self.cc)
