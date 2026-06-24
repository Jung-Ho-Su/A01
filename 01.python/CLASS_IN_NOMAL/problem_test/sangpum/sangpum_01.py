code = input("제품코드 입력 =>")
irum = input("제품명 입력 =>")
su = int(input("수량 입력 =>"))
price = int(input("단가 입력 =>"))

kumack = su * price

print("\n제품코드   제품명 수량  단가  판매금액")
print("============================================")
print("%4s  %4s %4d %4d %6d" % (code, irum, su, price, kumack))
print("============================================")