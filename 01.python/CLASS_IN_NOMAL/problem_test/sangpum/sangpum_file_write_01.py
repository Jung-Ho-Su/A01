# 제품코드, 제품명, 수량 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 sangpum_data.txt에 csv 형식으로 저장
#csv 파일은 모든 데이터를 ,으로 나누는 파일의 형태


fp = open('sangpum_data.txt', 'w', encoding='utf-8')
# w(write): 쓰기모드, r(read): 읽기모드, a(append): 추가모드 기존의 내용을 유지하면서 추가,
# b(binary): 2진 모드 , 2진수 형태로 저장 ex) wb, rb ab 로 binary 모드를 사용하는 방법으로 바이너리 모드는 무조건 b를 붙여야함
lst = [] # 빈 리스트의 용도 : 하나 또는 여러 개의 데이터를 저장하기 위한 용도

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

    fp.write(dct['code'] +","+ dct['irum'] +","+ str(dct['su']) +","+ str(dct['price']) + '\n')
    # write는 줄바꿈 기능이 없어서 줄바꿈 기능을 해주도록 적어줘야함

    print()

fp.close()
print("\n\t\t\t ***제품관리 ***")
print("\n제품코드   제품명 수량  단가  판매금액")
print("============================================")

total = 0 # 값을 누적할 때는 초기값을 준다. # 누적 변수는 반드시 초기화 작업이 필요하다.
for dct in lst:
    total += dct['price']
    print("%4s  %4s %4d %4d %6d" % (dct['code'], dct['irum'], dct['su'], dct['price'], dct['kumack']))
print("============================================")
print("\t\t\t\t\t 총금액 : %7d" % total)


# csv 파일