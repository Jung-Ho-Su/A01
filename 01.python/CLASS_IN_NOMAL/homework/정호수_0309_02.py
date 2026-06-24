class NumberError(Exception):
    def __init__(self):
        super().__init__("자릿수가 맞지 않습니다.")
class OverTimeError(Exception):
    def __init__(self):
        super().__init__('중복되어 사용할 수 없스니다.')
class MustUseUpper(Exception):
    def __init__(self):
        super().__init__('대문자를 사용해주세요')
class MustUseNumber(Exception):
    def __init__(self):
        super().__init__('정수를 입력해주세요')
class MustUseString(Exception):
    def __init__(self):
        super().__init__('문자를 입력해주세요')
class NegativeError(Exception):
    def __init__(self):
        super().__init__('음수는 사용하실 수 없습니다.')
class CantUseNumber(Exception):
    def __init__(self):
        super().__init__('숫자를 사용하실 수 없습니다.')
class RightRangeError(Exception):
    def __init__(self):
        super().__init__('1~6의 숫자를 입력하세요.')

used = []
class Sangpum():
    def __init__(self):
        self._code = ''
        self._name = ''
        self._su = 0
        self._price = 0
        self._kumack = 0
        self._total = 0

    def get_code(self):
        return self._code
    def set_code(self, code):
        self._code = code
    code = property(get_code, set_code)

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    name = property(get_name, set_name)

    def get_su(self):
        return self._su
    def set_su(self, su):
        self._su = su
    su = property(get_su, set_su)

    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price
    price = property(get_price, set_price)

    def get_kumack(self):
        return self._kumack
    def set_kumack(self, kumack):
        self._kumack = kumack
    kumack = property(get_kumack, set_kumack)

    def get_total(self):
        return self._total
    def set_total(self, total):
        self._total = total
    total = property(get_total, set_total)



    def input_data(self):
        global used

        while True: # 코드 예외 경우 : 4글자만, 글자마다 다른 경우, 중복
            try:
                self._code = input('상품 코드 입력 ==>')

                if len(self._code) != 4: #  자릿수가 4자리가 아닌 경우 에러
                    raise NumberError()

                if not self._code[0].isalpha(): # 코드 첫번째 문자가 아니고
                    raise MustUseString()
                if not self._code[0].isupper():   # 대문자가 아니고
                    raise MustUseUpper()
                for i in range(1, 4):           # 코드 뒤의 3자리가 숫자가 아닌 경우 에러
                    if not self._code[i].isdigit():
                        raise MustUseNumber()

                if self._code in used:                  # 코드가 중복된 경우
                    raise OverTimeError()

            except Exception as e:
                print('오류 발생!!', e)
            else:
                used.append(self._code)
                break


        while True:# 상품 이름 예외 경우 : 숫자인 경우
            try:
                self._name = input('상품 이름 입력 ==>')

                if self._name.isdigit(): # 이름에 숫자를 사용할 경우 에러
                    raise CantUseNumber()
                break
            except Exception as e:
                print('오류 발생!!', e)


        while True:# 수량 예외 경우 : 문자인 경우 , 음수인 경우
            try:
                su = input('상품 수량 입력 ==>')

                if not su.isdigit(): # 숫자가 문자인 경우 에러
                    raise MustUseNumber()
                self._su = int(su)
                if self._su < 0: # 수가 음수인 경우 에러
                    raise NegativeError()
                break
            except Exception as e:
                print('오류 발생!!', e)


        while True:# 상품 가격 예외 : 문자인 경우, 음수인 경우
            try:
                price = input('상품 가격 입력==>')
                if price.isalpha(): # 가격에 숫자를 사용하지 않을 경우 에러
                    raise MustUseNumber()
                self._price = int(price)
                if self.price < 0: #가격이 음수의 경우 에러
                    raise NegativeError()
                break
            except Exception as e:
                print('오류 발생!!', e)

    def update_data(self):


        while True:  # 코드 예외 경우 : 4글자만, 글자마다 다른 경우, 중복
            try:
                self._code = input('상품 코드 입력 ==>')

                if len(self._code) != 4:  # 자릿수가 4자리가 아닌 경우 에러
                    raise NumberError()

                if not self._code[0].isalpha():  # 코드 첫번째 문자가 아니고
                    raise MustUseString()
                if not self._code[0].isupper():  # 대문자가 아니고
                    raise MustUseUpper()
                for i in range(1, 4):  # 코드 뒤의 3자리가 숫자가 아닌 경우 에러
                    if not self._code[i].isdigit():
                        raise MustUseNumber()

                if self._code in used:  # 코드가 중복된 경우
                    raise OverTimeError()

            except Exception as e:
                print('오류 발생!!', e)
            else:
                used.append(self._code)
                break

        while True:  # 상품 이름 예외 경우 : 숫자인 경우
            try:
                self._name = input('상품 이름 입력 ==>')

                if self._name.isdigit():  # 이름에 숫자를 사용할 경우 에러
                    raise CantUseNumber()
                break
            except Exception as e:
                print('오류 발생!!', e)

        while True:  # 수량 예외 경우 : 문자인 경우 , 음수인 경우
            try:
                su = input('상품 수량 입력 ==>')

                if not su.isdigit():  # 숫자가 문자인 경우 에러
                    raise MustUseNumber()
                self._su = int(su)
                if self._su < 0:  # 수가 음수인 경우 에러
                    raise NegativeError()
                break
            except Exception as e:
                print('오류 발생!!', e)

        while True:  # 상품 가격 예외 : 문자인 경우, 음수인 경우
            try:
                price = input('상품 가격 입력==>')
                if price.isalpha():  # 가격에 숫자를 사용하지 않을 경우 에러
                    raise MustUseNumber()
                self._price = int(price)
                if self.price < 0:  # 가격이 음수의 경우 에러
                    raise NegativeError()
                break
            except Exception as e:
                print('오류 발생!!', e)

    def process_data(self):
        self._kumack = self._price * self._su



    def output_data(self):

        print("%4s  %4s  %4s  %4s  %4s" %
              (self._code, self._name, self._price, self._su, self._kumack))


if __name__ == "__main__":
  obj = Sangpum()
  obj.input_data()
  obj.process_data()
  print("\n\t\t\t *** 상품정보 ***")
  print("==============================================")
  print("상품코드 상품명 수량 가격 금액")
  print("==============================================")
  obj.output_data()
  print("===============================================")
