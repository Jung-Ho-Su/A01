# 예외를 새로 만드는 이유
# 프로그래머가 필요한 얘외 상황에 맞는 에러에 대한 클래스 이름을
# 명확하게 구분하고 알기 위해 이렇게 예외릘 만들어주는 작업을 한다.

class NotThreeMultipleError(Exception): #Exception을 상속받아서 새로운 예외로 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

def three_multiple():
    try:
        x = int(input('3의 배수를 이비력하세요:'))
        if x % 3 != 0:                  #x 가 3의 배수가 아니면
            raise NotThreeMultipleError #NotThreeMultipleError 예외를 발생시킴
        print(x)

    except NotThreeMultipleError as e:
        print('예외가 발생했습니다.1', e)

    except Exception as e:
        print('예외가 발생했습니다.2', e)

three_multiple()