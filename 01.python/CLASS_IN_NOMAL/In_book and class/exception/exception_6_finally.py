try:
    x= int(input('나눌 숫자를 입력하세요:'))
    y= 10/x
except ZeroDivisionError:   # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
except: # 앞에서 기술한 예외를 제외한 나머지 모든 예외 처리
    print("모든 예외 처리")
else:                       # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                    # 예외 발생 여부와 상관없이 항상 실행됨
    print("코드 실행이 끝났습니다.")