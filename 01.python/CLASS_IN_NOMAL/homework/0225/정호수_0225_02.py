
frist = int(input("첫번째 숫자를 입력하시오"))
second = int(input("두번째 숫자를 입력하시오"))

if frist > second:
    for i in range(second, frist + 1):
        print(f'\n**{i}단**')
        for n in range(1, 10):
            i*n
            print(f'{i} * {n} =',i*n)
else:
    for i in range(frist, second + 1):
        print(f'\n**{i}단**')
        for n in range(1, 10):
            i*n
            print(f'{i} * {n} =',i*n)




