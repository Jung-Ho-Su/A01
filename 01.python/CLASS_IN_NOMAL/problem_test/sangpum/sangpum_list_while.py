lst_rec = []


while True:
    lst = []
    lst.append(input("제품코드를 입력"))
    # if lst[0].lower() == "exit":
    #     break
    if 'exit' in lst:
        break
    lst.append(input("제품명를 입력"))
    lst.append(int(input("수량을 입력")))
    lst.append(int(input("단가를 입력")))

    lst.append(lst[2]*lst[3]) # while 문에서 작성하는 리스트의 index임 그렇기에 밖에 있는 lst_rec의 인덱스와는 상관없음
    lst_rec.append(lst)
    print()

print("\n제품코드   제품명 수량  단가  판매금액")
print("============================================")
total = 0
for lst in lst_rec:
    total += lst[4]
    print("%4s   %4s %4d    %4d   %6d" % (lst[0],lst[1],lst[2],lst[3],lst[4]))
print("============================================")
print("\t\t\t\t\t\t 총금액 : %d" % total)



#
# lst = []
# lst.append(input("제품코드를 입력"))
# lst.append(input("제품명를 입력"))
# lst.append(int(input("수량을 입력")))
# lst.append(int(input("단가를 입력")))
# lst.append(li[2]*li[3])