lst = []

while True:
    dct = {}
    dct['code'] = input("제품코드 입력 =>")
    if dct['code'].lower() == 'exit':
        break

    dct['irum'] = input("제품명 입력 =>")
    dct['su'] = int(input("수량 입력 =>"))
    dct['price'] = int(input("단가 입력 =>"))

    dct['kumack'] = (dct['su'] * dct['price'])

    lst.append(dct)
    print()

print("\n\t\t\t ***제품관리 ***")
print("\n제품코드   제품명 수량  단가  판매금액")
print("============================================")

total = 0 # 값을 누적할 때는 초기값을 준다.
for dct in lst:
    total += dct['price']
    print("%4s  %4s %4d %4d %6d" % (dct['code'], dct['irum'], dct['su'], dct['price'], dct['kumack']))
print("============================================")
print("\t\t\t\t\t 총금액 : %7d" % total)