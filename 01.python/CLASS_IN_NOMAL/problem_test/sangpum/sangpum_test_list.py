li = []

li.append(input("제품코드를 입력"))
li.append(input("제품명를 입력"))
li.append(int(input("수량을 입력")))
li.append(int(input("단가를 입력")))
li.append(li[2]*li[3])

print(li)

print("\n제품코드   제품명 수량  단가  판매금액")
print("============================================")
print("%4s   %4s %4d    %4d   %6d" % (li[0],li[1],li[2],li[3],li[4]))
print("============================================")



#
# lst = []
# lst.append(input("제품코드를 입력"))
# lst.append(input("제품명를 입력"))
# lst.append(int(input("수량을 입력")))
# lst.append(int(input("단가를 입력")))
# lst.append(li[2]*li[3])