y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index]/x)
except ZeroDivisionError as e:           # as 뒤에 변수를 지정하면 에러를 받아옴
    print('숫자를 0으로 나눌 수 없습니다.', e.args[0])  # e 에 저장된 에러 메시지 출력
    # args를 뒤에 붙여주면 오류에 좀 더 정확하게 접근 할 수 있다. 없어도 괜찮음
except IndexError as e:
    print('잘못된 인덱스입니다.', e.args[0])
except:
    print("나머지 예외 처리")