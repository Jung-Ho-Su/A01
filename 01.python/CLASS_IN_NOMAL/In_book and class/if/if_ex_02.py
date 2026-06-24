data = int(input("숫자를 입력하시오: "))

if data % 2 ==0:
    print("입력된 값은 짝수입니다.")
    if (data % 4) == 0:
        print("입력된 값은 4의 배수입니다.")
    else:
        print("입력된 값은 4의 배수가 아닙니다.")
else:
     print("입력된 값은 홀수입니다.")
     if(data % 4) == 0:
         print("입력된 값은 3의 배수입니다.")
     else:
         print("입력된 값은 3의 배수가 아닙니다.")


print("The End...")
