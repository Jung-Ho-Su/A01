# import os,sys
# print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test"))
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test"))
from 정호수_0306_02 import Sungjuk, RightRange

lst = []

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
  print()
  obj = Sungjuk()
  obj.input_sungjuk()
  obj.process_sungjuk()
  #global lst
  lst.append(obj)
  print("\n성적 입력 성공!!!\n")

def print_sungjuk():
  if len(lst) == 0:
    print("\n출력할 데이터가 없음!!\n")
    return

  print("\n\t\t\t *** 성적관리 ***")
  print("==============================================")
  print("학번   이름   국어   영어  수학   총점   평균  등급")
  print("==============================================")
  tot_avg = 0

  for obj in lst:
    obj.output_sungjuk()
    tot_avg += obj.avg # obj.avg => obj.get_avg()
  print("===============================================")
  print("\t\t\t 학생수: %d, 전체평균: %.2f\n" %
        (len(lst), tot_avg / len(lst)))

def search_sungjuk():
  if len(lst) == 0:
    print("\n조회할 데이터가 없음1!!\n")
    return

  hakbun = input("\n조회할 학번 입력 => ")
  for obj in lst:
    if obj.hakbun == hakbun:
      print("\n학번   이름   국어   영어  수학   총점   평균  등급")
      print("==============================================")
      obj.output_sungjuk()
      print("===============================================\n")
      break
  else:
    print("\n조회할 학생 정보가 없음2!!\n")


def update_sungjuk():
  if len(lst) == 0:
    print("\n수정할 데이터가 없음1!!\n")
    return

  hakbun = input("\n수정할 학번 입력 => ")
  for obj in lst:
    if obj.hakbun == hakbun:
      print()
      obj.update_sungjuk()
      obj.process_sungjuk()
      print("\n학번 %s 정보 수정 성공!!\n" % hakbun)
      break
  else:
    print("\n수정할 학생 정보가 없음2!!!\n")

def delete_sungjuk():
  if len(lst) == 0:
    print("\n삭제할 데이터가 없음1!!\n")
    return

  hakbun = input("\n삭제할 학번 입력 => ")
  for obj in lst:
    if obj.hakbun == hakbun:
      lst.remove(obj)
      print("\n학번 %s 정보 삭제 성공!!\n" % hakbun)
      break
  else:
    print("\n삭제할 학생 정보가 없음2!!!\n")

if __name__ == "__main__":
  while True:
    menu_title()
    try:
        menu = int(input("메뉴를 선택하세요(1~6) => "))
        if menu < 1 or menu > 6:
          raise RightRange()
    except Exception as e:
        print("\n숫자를 입력하세요!!!(%s)\n" % e)
        continue

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
