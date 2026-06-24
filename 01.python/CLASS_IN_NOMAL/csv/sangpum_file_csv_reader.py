import os # 운영체체기능과 관련된 모듈
import csv

if os.path.exists('sangpum_data.txt'):
    fp = open('sangpum_data.txt', 'r', encoding='utf-8', newline='') # r 모드는 해당 파일이 반드시 먼저 존재해야함
    reader = list(csv.reader(fp)) # 읽어온 데이터는 반복자 객체이고 이 읽어온 데이터를 리스트로 변형했다.
    lst = []
    for line in fp:
        dct = {}
        res = line.strip("\n").split(',')
        dct["code"] = res[0]
        dct["irum"] = res[1]
        dct["su"] = int(res[2])
        dct["price"] = int(res[3])

        dct['kumack'] = dct['su'] * dct['price']
        lst.append(dct)

    fp.close()

    print("\n\t\t\t ***제품관리 ***")
    print("\n제품코드   제품명 수량  단가  판매금액")
    print("============================================")

    total = 0 # 값을 누적할 때는 초기값을 준다.
    for dct in lst:
        total += dct['price']
        print("%4s  %4s %4d %4d %6d" % (dct['code'], dct['irum'], dct['su'], dct['price'], dct['kumack']))
    print("============================================")
    print("\t\t\t\t\t 총금액 : %7d" % total)

else:
    print("파일이 존재하지 않습니다.!!!")