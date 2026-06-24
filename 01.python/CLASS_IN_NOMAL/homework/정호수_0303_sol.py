def input_num():
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    return num1, num2

def  min_max_num(num1, num2):
    if num1 > num2:
        min_num = num2
        max_num = num1
    else:
        min_num = num1
        max_num = num2
    return min_num, max_num

def pri(min_num, max_num):
    print()

    cnt = 0
    for i in range(min_num, max_num + 1):
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:  # 소수인 경우 수행
            print("%5d " % (i), end="")
            cnt += 1  # 소수의 갯수 카운트
            if cnt % 10 == 0:  # 소수의 갯수가 10의 배수이면 줄바꿈 수행
                print()
    if cnt % 10 != 0:
        print()
        # 만약 출력된 소수의 개수가 10개가 되지 않으면 뒤에 출력되는 '총소수의 개수'가 같은 행으로 출력되는 것을
        # 방지해주기 위한 것이다.

    return cnt



def prime_num():
    print("총소수의 갯수 = %d" % (cnt))
    return


if __name__=="__main__":
    num1, num2 = input_num()
    min_num, max_num = min_max_num(num1, num2)
    cnt = pri(min_num, max_num)
    prime_num()