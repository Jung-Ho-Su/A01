from inhe import *

if __name__ == '__main__':
    obj = C() # c 클래스로 객체를 만들어 객체에 저장 # c는 b,a를 상속받아 ba 의 모든 속성을 사용 가능한 클래스
    print(obj.cc)
    print(obj.bb)
    print(obj.aa)
    print()
    obj.printA()
    obj.printB()
    obj.printC()