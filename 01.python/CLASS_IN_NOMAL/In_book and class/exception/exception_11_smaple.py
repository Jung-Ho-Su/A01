class AgeException(Exception):
    def __init__(self, msg1, msg2):
        self._message1 = msg1
        self._message2 = msg2

def input_age():
     age = int(input("나이를 입력해 주세요:"))

     if age < 0:
         raise AgeException("나이는 음수가 될 수 없습니다.", "헐")
     elif age > 150:
         raise AgeException("150세 이상 살 수 있을까요?", "um...")
     else:
         return age

if __name__ == '__main__':
    try:
        age = input_age()
    except AgeException as e:
        print(e.args)           # print(e), # print(e.args[0]) # args[1]
    else:
        print('나이는 %d세 입니다.' % age)
