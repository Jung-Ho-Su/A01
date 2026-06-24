frist = int(input("첫번째 숫자를 입력하시오"))
second = int(input("두번째 숫자를 입력하시오"))

if frist > second:
    for i in range(second, frist + 1):
        print(f'**{i}단**', end='\t')
    print()

    for n in range(1, 10):

        for i in range(second, frist + 1):
            print(f'{i}*{n} ={i*n}', end='\t')
        print()


else:
    for i in range(frist, second + 1):
        print(f'**{i}단**', end='\t')
    print()

    for n in range(1, 10):

        for i in range(frist, second + 1):
            print(f'{i}*{n} ={i*n}', end='\t')
        print()
