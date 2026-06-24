# 형식 매개변수 radius 와 print_format 에 실 매개변수 3과 lambda가 대입된다.
# 형식 매개변수 :
# 실매개변수 :
def circle_area(radius, print_format):
    area = 3.14 * (radius ** 2)
    print_format(area)

if __name__ == '__main__':
    a = lambda x : print("결과값:", round(x, 1))
    circle_area(3, a)
    circle_area(3, lambda x : print("결과값:", round(x, 2)))