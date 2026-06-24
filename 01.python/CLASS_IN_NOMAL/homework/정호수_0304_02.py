import csv
import os

def menu_title():
  print("*** 성적관리 ***")
  print("1. 성적정보 입력")
  print("2. 성적정보 출력")
  print("3. 성적정보 조회")
  print("4. 성적정보 수정")
  print("5. 성적정보 삭제")
  print("6. 프로그램 종료")
  print()

def input_sungjuk():
    if os.path.exists('../sungjuk_data.csv'):
        fp = open("../sungjuk_data.csv", "at", encoding="utf-8", newline='')
        fieldnames = ["num", "name", "kor", "eng", "math", "total", "avg", "grade"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
    else:
        fp = open("../sungjuk_data.csv", "at", encoding="utf-8", newline='')
        fieldnames = ["num", "name", "kor", "eng", "math", "total", "avg", "grade"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        wr.writeheader()

    dct = {}
    dct["num"] = input("\n학번 입력 => ")
    dct["name"] = input("이름 입력 => ")
    dct["kor"] = int(input("점수 입력 => "))
    dct["eng"] = int(input("점수 입력 => "))
    dct["math"] = int(input("점수 입력 => "))
    dct["total"] = int(dct["kor"] + dct["eng"] + dct["math"])
    dct["avg"] = dct["total"] / 3

    score = dct["avg"]
    if dct["avg"] >= 90:
        score = "수"
    elif dct["avg"] >= 80:
        score = "우"
    elif dct["avg"] >= 70:
        score = "미"
    elif dct["avg"] >= 60:
        score = "양"
    elif dct["avg"] < 60:
        score = "가"
    dct["grade"] = score


    wr.writerow(dct)
    fp.close()
    print("\n성적 입력 성공!!\n")

def print_sungjuk():
  if os.path.exists('../sungjuk_data.csv'):
    fp = open("../sungjuk_data.csv", "r", encoding="utf-8", newline='')
    lst = list(csv.DictReader(fp))

    print("\n\t\t\t *** 성적관리 ***")
    print("=============================================")
    print("학번    이름   국어 영어 수학  총점  평균  등급")
    print("=============================================")
    su = 0
    all_avg = 0
    for data in lst:
      su += 1
      all_avg += (float(data["avg"])/su)
      print("%2s     %3s  %d  %d  %d   %2d  %2.2f %2s" %
            (data["num"], data["name"], int(data["kor"]),
             int(data["eng"]), int(data["math"]), int(data['total']), float(data['avg']), data['grade']))
    print("=============================================")
    print("\t\t\t 학생수 : %2d     전체 평균 : %2.2f\n" % (su, all_avg))

    fp.close()
  else:
    print("\n출력할 제품 정보가 없음!!!\n")


def search_sungjuk():
    if os.path.exists('../sungjuk_data.csv'):
        fp = open("../sungjuk_data.csv", "r", encoding="utf-8", newline='')
        lst = list(csv.DictReader(fp))
        code = input("\n조회할 학번 입력 => ")
        for data in lst:
            if data["num"] == code:
                print("\n학번    이름   국어 영어 수학  총점  평균 등급")
                print("=============================================")
                print("%2s     %3s  %d  %d  %d   %2d  %2.2f %2s" %
                      (data["num"], data["name"], int(data["kor"]),
                       int(data["eng"]), int(data["math"]), int(data['total']), float(data['avg']), data['grade']))
                print("=============================================\n")
                break
        else:
            print("\n조회할 학생 정보가 없음2!!!\n")
        fp.close()
    else:
        print("\n조회할 학생 정보가 없음1!!!\n")

def update_sungjuk():
    if os.path.exists('../sungjuk_data.csv'):
        fp = open('../sungjuk_data.csv', 'r', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
        lst = list(csv.DictReader(fp))
        code = input("\n점수를 수정할 학번 입력 ==>")


        flag = 0
        for data in lst:

            if data["num"] == code:
                data["kor"] = int(input("수정할 국어 점수 입력=>"))
                data["eng"] = int(input("수정할 영어 점수 입력=>"))
                data["math"] = int(input("수정할 수학 점수 입력=>"))
                data["total"] = int(data["kor"] + data["eng"] + data["math"])
                data["avg"] = data["total"] / 3
                flag = 1
                break
        else:
            print("\n수정할 정보가 없음!!!\n")


        if flag == 1:
            fp2 = open('../sungjuk_data.csv', 'wt', encoding='utf-8', newline='')
            fieldnames = ["num", "name", "kor", "eng", "math", "total", "avg", "grade"]
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)
            fp2.close()
        else:
            print("\n수정할 제품 정보가 없음!!\n")

def delete_sungjuk():
  if os.path.exists('../sungjuk_data.csv'):
    fp = open('../sungjuk_data.csv', 'r', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
    lst = list(csv.DictReader(fp))
    num = input("\n삭제할 학생 학번 입력 ==>")
    flag = 0
    for data in lst:
      if data["num"] == num:
        lst.remove(data)
        print("\n학번 %s 학생 정보 삭제\n" % num)
        flag = 1
        break
    else:
      print("\n삭제할 정보가 없음!!!\n")
    fp.close()

    if flag == 1:
      fp2 = open('../sungjuk_data.csv', 'wt', encoding='utf-8', newline='')
      fieldnames = ["num", "name", "kor", "eng", "math", "total", "avg", "grade"]
      wr = csv.DictWriter(fp2, fieldnames=fieldnames)
      wr.writeheader()
      wr.writerows(lst)
      fp2.close()
    else:
      print("\n수정할 제품 정보가 없음!!\n")


if __name__ == "__main__":
  while True:
    menu_title()
    menu = int(input("메뉴를 선택하세요(1~6) => "))
    if menu == 1:
      input_sungjuk()
    elif menu == 2:
      print_sungjuk()
    elif menu == 3:
      search_sungjuk()
    elif menu == 4:
      update_sungjuk()
    elif menu == 5:
      delete_sungjuk()
    elif menu == 6:
      print("\n프로그램 종료!!")
      break
    else:
      print("\n메뉴를 다시 입력하세요!!\n")
