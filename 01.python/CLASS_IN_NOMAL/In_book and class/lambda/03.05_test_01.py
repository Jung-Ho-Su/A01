#2026.03.05
#unit 32

# 람다 뒤에 변수가 2개 이니 이것은 파라매터가 2개라는 뜻
# 이걸 변수에 저장하고 변수를 호출해서 함수를 시행 가능
# return 이 없고 : 뒤에 수식의 값이 자동으로 반환된다
circle_area = lambda radius, pi:pi * (radius ** 2)
print(circle_area(3, 3.14))