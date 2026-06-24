num1 = int(input("첫번째 숫자를 입력하시오"))
num2 = int(input("두번째 숫자를 입력하시오"))

if num1 > num2:
    min_num = num2
    max_num = num1
else:
    min_num = num1
    max_num = num2

for i in range(min_num, max_num +1):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print("%5d" % (i), end="")
        cnt += 1
        if cut % 10 == 0:
            print()

if cnt % 10 != 0:
    print()

print("총소수의 갯수 = %d" % (cnt))