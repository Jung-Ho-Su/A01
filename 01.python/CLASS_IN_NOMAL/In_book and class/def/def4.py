def circle_area(r): # r = 지역 변수
    result = 3.14 * (r ** 2) # result = 지역 변수
    return result


if __name__ == '__main__':
    radius = 3 # 전역 변수
    area = circle_area(radius) # 전역 변수
    print("반지름 : %d, 면접 : %2f" % (radius, area))
    print(r)

# 함수에서 변수를 정의한 뒤 그 변수는 함수 내에서만 사용이 가능하고
# 함수 범위 내에서 벗어나면 그 변수는 사용이 불가능해진다
# 위 내용에서 r의 변수가 그러하다.