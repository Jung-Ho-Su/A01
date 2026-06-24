#2026.03.04
# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 sangpum_data.txt에 csv형식으로 저장
import csv
import os

def menu_title():
    print("*** 제품 관리 ***")
    print("1. 제품 정보 입력")
    print("2. 제품 정보 출력")
    print("3. 제품 정보 조회")
    print("4. 제품 정보 수정")
    print("5. 제품 정보 삭제")
    print("6. 프로그램 종료")
    print()

# 데이터를 입력받고, 나중에 쓰게 되면 추가하려고 한다 그렇기에 a 모드를 사용할것
def input_data(): # 데이터를 입력하고 저장되고 추후에 추가도 되는 함수
    if os.path.exists('../../sangpum_data.csv'):
        fp = open('../../sangpum_data.csv', 'at', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
        fieldnames = ['code', 'irum', 'su', 'price', 'kumack']
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
    else:
        fp = open('../../sangpum_data.csv', 'at', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
        fieldnames = ['code', 'irum', 'su', 'price', 'kumack']
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        wr.writeheader()

    dct = {}
    dct["code"] = input("제품코드 입력 => ")
    dct["irum"] = input("제품명 입력 => ")
    dct["su"] = int(input("수량 입력 => "))
    dct["price"] = int(input("단가 입력 => "))

    dct["kumack"] = dct["su"] * dct["price"]
    wr.writerow(dct)
# writerow로 하면 문자열로 바뀌게 되어버림
    fp.close()
    print("\n제품정보 입력 성공!!\n")

def print_data(): # 파일에 입력된 데이터를 읽어들이고 출력하는 함수
    if os.path.exists('../../sangpum_data.csv'):
        fp = open('../../sangpum_data.csv', 'r', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
        lst = list(csv.DictReader(fp))
        # 반복자 객체lst = csv.DictReader(fp)가 되어서 다시 읽지 못하기에 list의 형태로 변형시켜서 읽어주면
        # 다음에 다시 읽을 수 있다
        # DictReader로 읽기 위해서는 해당 필드 위에 key가 먼저 나와야한다.



        # csv.reader에서 reader 를 사용하면 파일을 list 형태로 읽어들인다.
        # list(csv.reader)로 적었으니 리스트 형태로 읽어들인 파일을 list 형태로 만든 형태이다.
        # 즉, list안에 list가 입력한 제품의 수 만큼 들어간 형식

        print(lst) # 구조 확인용

        print("\n\t\t\t *** 제품관리 ***")
        print("=============================================")
        print("제품코드   제품명     수량      단가    판매금액")
        print("=============================================")
        total = 0
        for data in lst:
            total += int(data["kumack"])
            print("%4s     %4s    %4d    %4d    %6d" %
                  (data["code"], data["irum"], int(data["su"]), int(data["price"]), int(data["kumack"])))
        print("=============================================")
        print("\t\t\t\t\t\t 총금액 : %7d" % total)

        fp.close()
    else:
        print("\n출력할 제품 정보가 없어!!\n")


def search_data():
    # 제품 코드를 입력받아 해당 제품 정보를 출력한다.
    if os.path.exists('../../sangpum_data.csv'):
        fp = open('../../sangpum_data.csv', 'r', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
        lst = list(csv.DictReader(fp))
        code = input("\n조회할 제품코드 입력 ==>")

        for data in lst:
            if data["code"] == code:
                print("\n제품코드   제품명     수량      단가    판매금액")
                print("=============================================")
                print("%4s     %4s    %4d    %4d    %6d" %
                      (data["code"], data["irum"], int(data["su"]), int(data["price"]), int(data["kumack"])))
            print("=============================================\n")
            break
        else:
            print("\n조회할 제품 정보가 없음2!!!")
        fp.close()
    else:
        print("\n조회할 제품 정보가 없음1!!!")




def update_data():
    # 제품코드를 입력받아 일치하는 데이터를 찾아서 수량과 단가를 입력받아 금액을 수정 후 파일 전체를 재저장
    if os.path.exists('../../sangpum_data.csv'):
        fp = open('../../sangpum_data.csv', 'r', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
        lst = list(csv.DictReader(fp))
        code = input("\n조회할 제품코드 입력 ==>")
        flag = 0
        for data in lst:
            if data["code"] == code:
                data["su"] = int(input("수량 입력=>"))
                data["price"] = int(input("단가 입력=>"))
                data["kumack"] = data["su"] * data["price"]
                flag = 1
                break
        else:
            print("\n수정할 정보가 없음!!!\n")


        if flag == 1:
            fp2 = open('../../sangpum_data.csv', 'wt', encoding='utf-8', newline='')
            fieldnames = ['code', 'irum', 'su', 'price', 'kumack']
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)
            fp2.close()
        else:
            print("\n수정할 제품 정보가 없음!!\n")

def delete_data():
    if os.path.exists('../../sangpum_data.csv'):
        fp = open('../../sangpum_data.csv', 'r', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
        lst = list(csv.DictReader(fp))
        code = input("\n삭제할 제품 코드를 입력하세요 ==>")
        flag = 0
        for data in lst:
            if data["code"] == code:
                flag = 1
                break
        else:
            print("\n삭제할 정보가 없음!!!\n")

        if flag == 1:
            fp2 = open('../../sangpum_data.csv', 'wt', encoding='utf-8', newline='')
            fieldnames = ['code', 'irum', 'su', 'price', 'kumack']
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)
            fp2.close()
        else:
            print("\n삭제할 제품 정보가 없음!!\n")



if __name__=="__main__":
    while True:
        menu_title()

        menu = int(input("메뉴를 선택하세요(1~6) ==>"))
        if menu == 1:
            input_data()
        elif menu == 2:
            print_data()
        elif menu == 3:
            search_data()
        elif menu == 4:
            update_data()
        elif menu == 5:
            delete_data()
        elif menu == 6:
            print("\n프로그램 종료!!\n")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")