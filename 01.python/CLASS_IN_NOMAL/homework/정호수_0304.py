import csv #csv 불러와서 csv 함수를 불러 올 수 있게 함
import os # os 운영 체제를 불러와서 윈도우 함수를 쓸 수 있게 함

#터미널에서 반복적으로 출력할 내용을 함수로 만들어서 if __name__="__main__" 문에서 출력할 때 편하게 출력할 수 있게
#하기 위해 함수로 만듦

def menu_title():
  print("*** 성적관리 ***")
  print("1. 성적정보 입력")
  print("2. 성적정보 출력")
  print("3. 성적정보 조회")
  print("4. 성적정보 수정")
  print("5. 성적정보 삭제")
  print("6. 프로그램 종료")
  print()


# 성적을 입력하는 함수를 input_sungjuk이라는 함수로 표현함
def input_sungjuk():
    #윈도우 os 체제에서 현재 프로그램을 위치 기준으로 한 단계 위 폴더에 있는
    #sungjuk_data.csv라는 파일이 있는지 확인하는 작업을 거침
    #()안에는 경로를 적어야하며 해당 경로에 파일이 있거나 폴더가 있으면
    #True 반환 없으면 False를 반환하는 불대수 함수임
    # 파일을 옮기니 ../ 이라는 체제가 생겼는데 이것은 한 단계 위의 파일을 의미함
    # 예상컨데 한 단계 위의 파일에 txt파일이 남아 있어서 그런 것으로 추정
    # 만약, 파일이 해당 경로에 존재하지 않고 ../ 가 없고 현재 파일에도 txt 파일이 없다면
    # 새로운 txt 파일이 만들어짐
    if os.path.exists('../sungjuk_data.csv'):
        # fp 라는 변수에 해당 파일을 열어서 파일 객체를 저장한다는 의미
        # ../sungjuk_data.csv : 해당 경로의 파일을 연다
        # at : append txt 내용을 추가하는 append 모드로 파일을 열것이다.
        # encoding='utf-' : utf-8로 인코딩을 해서 txt 파일을열었을 때 오류가 없게 한다
        # newline='' : csv 파일에서 줄바꿈이 두 번 들어가는 문제를방지하기 위해 사용
        # csv + os 줄바꿈 방식 : \r\n이 자동으로 일어난다 그렇기에 파이선이 자동으로 줄바꿈을해버린다.
        # 그렇기에 newline 이라는 함수를 이용해 csv + os 에서 줄바꿈이 일어나 가독성을 해치기 때문에
        # newline=''을 써서 줄바꿈을 한번만 일어나게 해준다.
        fp = open("../sungjuk_data.csv", "at", encoding="utf-8", newline='')
        # fieldnams는 그냥 파이선 리스트 변수 그냥 변수에 리스트 형식으로 문자를 저장한 것이다.
        fieldnames = ["num", "name", "kor", "eng", "math", "total", "avg", "grade"]
        # csv는 모듈 안의 클래스이다. csv 클래스를 이용하기 위해 1 행에서 import csv 를 해서 불러오고
        # DictWriter 이라는 csv 내장 함수 를 쓰기 위해 csv.DictWriter의 형태를 표현함
        # DictWriter를 쓰면 딕셔너리의 key가 csv 컬럼으로 자동 maping 된다.
        # 즉, 이 함수를 쓰면 해당 파일 객체에 딕셔너리 형태로 csv 컬럼의 1행에 key 가 저장된다.
        # 출력 객체를 만드는 과정
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
    else:
        #이 항목은 파일이 없을 경우이기 때문에 wt 를 사용해도 상관없다
        fp = open("../sungjuk_data.csv", "at", encoding="utf-8", newline='')
        fieldnames = ["num", "name", "kor", "eng", "math", "total", "avg", "grade"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        # 해당 파일이 경로에 존재하지 않을 경우는 새롭게 파일을 만들어야 하는데 파일을 만들게 되고
        # 각 줄의 컬럼의 이름을 정하고 첫 줄에는 컬럼의 이름만 들어가고 다른 정보다 두번째 행부터 들어오게
        # 하기 위함 또한 이를 사용하지 않으면 csv 컬럼과 딕셔너리 key가 맞지 않아 keyerror가 발생 가능
        # fieldnames을 맨 위에 써주는 기능을 한다. [맨 위 고정]
        # DictWriter를 사용할 때는, 최초 출력을 할 때는 , wr.writeheader가 필요하다.
        wr.writeheader()
# 성적을 하나만 입력하기 때문에 반복문을 돌릴 필요가 없다
    dct = {}
    dct["num"] = input("\n학번 입력 => ")
    dct["name"] = input("이름 입력 => ")
    dct["kor"] = int(input("점수 입력 => "))
    dct["eng"] = int(input("점수 입력 => "))
    dct["math"] = int(input("점수 입력 => "))
    dct["total"] = int(dct["kor"] + dct["eng"] + dct["math"])
    dct["avg"] = dct["total"] / 3

# 개인의 평균에 등급을 내주기 위한 것으로 if 문을 이용해서 각 범위에 따른 등급을 설정함
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

    #wr은 csv파일에서 딕셔너리를 한 줄 씩 저장하는 명령어이다.
    #그래서 () 안에 dct딕셔너리를 넣어서 앞에서 저장한 딕셔너리를
    #csv파일에 dct 형태의 fieldnames을 저장하는 역할을 한다.
    # 즉, 우리가 입력한 값을 csv파일에 저장하는 역할
    # --s 가 없는 거는 딕셔너리 객체 하나만 출력하는 것
    wr.writerow(dct)
    # 파일을 열었으니 닫아준다.
    fp.close()
    print("\n성적 입력 성공!!\n")

def print_sungjuk():
  if os.path.exists('../sungjuk_data.csv'):
    fp = open("../sungjuk_data.csv", "r", encoding="utf-8", newline='')
    #Dictreader() : 는 csv  파일을 읽어서 딕셔너리 단위로 만들어주는 역할을 하는 함수로
    # 한 줄 씩 읽어서 딕셔너리로 반환한다.
    # 즉, csv의 각 행이 딕셔너리로 변환된다.
    # 여기서 DictReader(fp)는 "반복자 객체" 라는 녀석으로
    # 특징 1. 한방향으로 진행하는 특징이 있고
    # 2. 어떤 값을 꺼낼 때 한 개 한 개씩만 꺼낼 수 있음
    # 3. 한 번 꺼낸(지나간) 객체는 다시 사용하지 못함

    # 여기서 3번 특성 때문에 csv.DictReader(fp)를 그냥 사용하면
    # 한 번 사용하고 끝이기에 list 형태로 만들어서 lst 변수에 담아
    # 다시 사용할 수 있게 변환
    lst = list(csv.DictReader(fp))

    print("\n\t\t\t *** 제품관리 ***")
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
        # 여기서는 상품을 서치하는 함수이기 때문에 fp 에서 r =read 모드로 그냥 읽기만 하기로 함수를 정의함
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

    # 파일 존재의 유무를 검사할 때 파일이 없다면 조회 정보가 없다고 알려주는 용도의 if 문의 else 이다.
    else:
        print("\n조회할 학생 정보가 없음1!!!\n")



# 업데이트 부분에서 수정되기 전의 내용을 lst의 리스트 안에 저장하고 저장된 내용을
# for 문을 반복해서 lst 의 내용을 수정한다 그렇게 for문을 마치면 lst 안에 자동으로 수정된 내용이
# 기록되고 이제 lst안에는 변경된 즉, update 된 내용이 담겨있을 것이다.
# 이제 이 업데이트 된 lst를 기존에 파일의 내용을 모두 지우고 wt 의 모드를 써서
# 다시 작성해주면 된다.
def update_sungjuk():
    if os.path.exists('../sungjuk_data.csv'):
        #일단 먼저 파일을 먼저 읽고 난 다음에 어떤 값을 수정할지 바꿀지 알 수 있기에 먼저 파일을 읽는 r 모드로 실행
        fp = open('../sungjuk_data.csv', 'r', encoding='utf-8', newline='')  # r 모드는 해당 파일이 반드시 먼저 존재해야함
        # fp 파일을 읽고 반복자 객체로 나타난 csv 파일을 리스트 형태로 저장
        lst = list(csv.DictReader(fp))
        code = input("\n점수를 수정할 학번 입력 ==>")

        # 현재 파일을 읽기만 한 상태이고 아직 수정하지 않은 것을 컴퓨터(파이선)에게 알려주기 위해서 불리언 수를 가장
        # 대표적으로 나타내는 0과 1을 사용해서 flag 라는 함수에 수를 할당함
        flag = 0
        for data in lst:
            # 만약 앞서 입력한 code가 csv 안의 num의 키와 일치한다며녀 if 문이 실행되어 수정후 들어갈 내용을 입력하고
            # 입력한 뒤에는 일단 수정을 행했다는 의미이기에 if 문을 마치면 flag = 1 이라는 뜻으로 정리한다.
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
        # 여기서는 앞서 수정할 데이터가 다 완료되고 나면 flag 가 1로 바뀌고 난 뒤
        # flag 가 1이 되면 파일을 wt 모드로 작성해서 새롭게 변경된 내용을 입력하라는 의미임
        # 앞선 첫번째 input함수에서 정의한 것 처럼 현재 새롭게 파일을 만들고 있으니 새롭게 모든 함수(행)들을 다 써줘야함
        if flag == 1:
            fp2 = open('../sungjuk_data.csv', 'wt', encoding='utf-8', newline='')
            fieldnames = ["num", "name", "kor", "eng", "math", "total", "avg", "grade"]
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            #이 줄이 없으면 fieldnames 이 정의되지 않아서 나중에 데이터를 읽을 때 열 이름이 없어서
            # csv.DictWriter가 제대로 작동하지 않을 수도 있다
            wr.writeheader()
            # lst라는 리스트 안의 내용을 행에 한 줄 씩 기록한다.
            wr.writerows(lst)
            fp2.close()
        else:
            print("\n수정할 제품 정보가 없음!!\n")


# 이것도 업데이트와 같은 형식으로 진행된다.
# lst의 리스트에 저장된 기존의 정보를 remove의 리스트 함수를 사용해서 제거하고 이후에
# 변경된 내용이 lst 안에 저장되면 이를 다시 flag=1 이 되었을 때를 if 로 가정해서 wt모드로 다시 작성해주면 된다.
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
