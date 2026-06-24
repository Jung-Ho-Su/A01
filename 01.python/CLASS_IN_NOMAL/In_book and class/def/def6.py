pi = 3.14

def circle_area(r): # r은 형식매개변수이자 지역변수
    # circle_area_with_pi의 local 영역
    global pi # 특정한 영역에서 전역 변수를 사용해주고싶을 때 사용
    # 전역 변수 pi를 참조한다는 선언문
    # 이렇게 되면 pi 라는 이름으로 함수 내에서 지역 변수를 못 만든다

    pi = pi + 0.0015
    return pi * (r**2)
    return HRESULT

if __name__ == '__main__':
    print("PI:", pi)
    print("반지름:",3, "면적:", circle_area(3))
    print("PI:", pi)