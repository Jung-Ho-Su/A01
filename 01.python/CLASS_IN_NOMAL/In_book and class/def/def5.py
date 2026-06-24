# 함수를 여러개 실행할 때 어떤 함수는 지역변수, 전역변수를 참조하는지 그 흐름을 이해하기


pi = 3.1415 # 이렇게 해주면 def4와 달리 import를 해줄 수 있다.

def circle_area_with_pi(r):
    #circle_area_with_pi의 local영역
    pi = 3.14
    result = pi*(r**2)
    return result

def circle_area_without_pi(r):
    #circle_area_without_pi의 local 영역
    result = pi*(r**2)
    return result

def sum_areas():
    result = [circle_area_with_pi(3), circle_area_without_pi(3)]
    return sum(result)                # built-in의 sum 함수를 호출

if __name__ == '__main__':
    print("PI", pi)
    print("반지름:", 3, "면적:", circle_area_with_pi(3))
    print("반지름:", 3, "면적:", circle_area_without_pi(3))
    print(sum_areas())