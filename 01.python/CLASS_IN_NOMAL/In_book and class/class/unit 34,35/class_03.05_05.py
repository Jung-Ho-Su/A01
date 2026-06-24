class Person:
    def __init__(self, name, age, address, wallet):
        self._name = name
        self._age = age
        self._address = address
        self._wallet = wallet #변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    name = property(get_name, set_name)

    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age
    age = property(get_age, set_age)

    def get_address(self):
        return self._address
    def set_address(self, address):
        self._address = address
    address = property(get_address, set_address)

    def get_wallet(self):
        return self._wallet
    def set_wallet(self, wallet):
        self._wallet = wallet
    wallet = property(get_wallet, set_wallet)

    def pay(self, amount):
        self._wallett -= amount # 비공개 속성은 클래스 안의 매서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self._wallet))

if __name__=="__main__":
    maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
    print(maria.name)
    maria.name = "이기자"
    print(maria.name)