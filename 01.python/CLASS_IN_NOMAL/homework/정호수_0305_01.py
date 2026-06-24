from sungjuk_class_0305 import Sungjuk

lst = [] # 전역변수

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
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    lst.append(obj)
    print("\n성적 입력 성공!!!\n")

def print_sungjuk():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음!!!\n")
        return

    print("\n\t\t\t *** 성적관리 ***")
    print("=============================================")
    print("학번    이름   국어 영어 수학  총점  평균  등급")
    print("=============================================")
    tot_avg = 0

    for obj in lst:
        obj.output_sungjuk()
        tot_avg += obj.avg # obj.avg = > obj.get.avg()가 참조되는 것이기 때문에 이렇게 적어도 무관하다
    print("=============================================")
    print("\t\t\t 학생수 : %2d, 전체 평균 : %2.2f\n" % (len(lst), tot_avg / len(lst)))


def search_sungjuk():
    # class 함수 불러오기
    code = input("학번을 입력하시오")
    for obj in lst:
        if obj.get_hakbun == code:
            print("\n\t\t\t *** 성적관리 ***")
            print("=============================================")
            print("학번    이름   국어 영어 수학  총점  평균  등급")
            obj.output_sungjuk()
            print("=============================================")
            return
    else:
        print("학생 정보 없음")

def update_sungjuk():
    code = input("\n점수를 수정할 학번 입력 ==>")
    for obj in lst:
        if obj.hakbun == code:
            obj.kor = int(input("수정할 국어 점수 입력=>"))
            obj.eng = int(input("수정할 영어 점수 입력=>"))
            obj.math = int(input("수정할 수학 점수 입력=>"))
            obj.process_sungjuk()



def delete_sungjuk():
    code = input("\n점수를 삭제할 학번 입력 ==>")
    for obj in lst:
        if obj.hakbun == code:
            lst.remove(obj)
            obj.process_sungjuk()


if __name__ == '__main__':
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