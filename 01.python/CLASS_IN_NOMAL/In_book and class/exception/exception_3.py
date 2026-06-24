y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index]/x)
except ZeroDivisionError:           # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:                  #범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.')
except:                             # 위의 두 예외처보다 마지막에 위치한 전체 예외처리는 마지막에 위치해야 나머지에 대한 예외를 다 처리할 수 있다.
    print("나머지 예외 처리")