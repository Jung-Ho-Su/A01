num_1 = int(input("첫번째 숫자를 입력하시오."))
num_2 = int(input("두번째 숫자를 입력하시오."))

prime = []

if num_1 < 2:
    num_1 = 2
if num_2 < 2:
    num_2 = 2

if num_1 > num_2:
    for i in range(num_2, num_1+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i) 
            if len(prime) % 10 == 0:
                print("%4d" % i)
            else:
                print("%4d" % i, end=" ")

if num_2 > num_1:
    for i in range(num_1, num_2+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
            if len(prime) % 10 == 0:
                print("%4d" % i)
            else:
                print("%4d" % i, end=" ")

print("\n총소수의 갯수 :", len(prime))