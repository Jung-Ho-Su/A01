from 정호수_0309_02 import RightRangeError,Sangpum

lst = []

def menu_title():
  print("*** 성적관리 ***")
  print("1. 상품정보 입력")
  print("2. 상품정보 출력")
  print("3. 상품정보 조회")
  print("4. 상품정보 수정")
  print("5. 상품정보 삭제")
  print("6. 프로그램 종료")
  print()

def input_data():
  print()
  obj = Sangpum()
  obj.input_data()
  obj.process_data()
  #global lst
  lst.append(obj)
  print("\n상품 정보 입력 성공!!!\n")

def print_data():
  obj = Sangpum()
  if len(lst) == 0:
    print("\n출력할 데이터가 없음!!\n")
    return

  print("\n\t\t\t *** 상품정보 ***")
  print("==============================================")
  print("상품코드 상품명    수량   가격   금액")
  print("==============================================")
  total = 0
  for obj in lst:
    obj.output_data()
    total += obj.kumack
  print("==============================================")
  print("\t\t\t 총금액 : %7d" % total)


def search_data():
  if len(lst) == 0:
    print("\n조회할 데이터가 없음1!!\n")
    return

  code = input("\n조회할 학번 입력 => ")
  for obj in lst:
    if obj.code == code:
      print("===============================================")
      print("상품코드 상품명 수량 가격 금액")
      print("===============================================")
      obj.output_data()
      print("===============================================\n")
      break
  else:
    print("\n조회할 상품 없음2!!\n")


def update_data():
  if len(lst) == 0:
    print("\n수정할 데이터가 없음1!!\n")
    return

  code = input("\n수정할 상품코드 입력 => ")
  for obj in lst:
    if obj.code == code:
      print()
      obj.update_data()
      obj.process_data()
      print("\n상품코드 %s 정보 수정 성공!!\n" % code)
      break
  else:
    print("\n수정할 상품 없음2!!!\n")

def delete_data():
  if len(lst) == 0:
    print("\n삭제할 데이터가 없음1!!\n")
    return

  code = input("\n삭제할 상품코드 입력 => ")
  for obj in lst:
    if obj.code == code:
      lst.remove(obj)
      print("\n상품코드 %s 정보 삭제 성공!!\n" % code)
      break
  else:
    print("\n삭제할 상품 없음2!!!\n")

if __name__ == "__main__":
  while True:
    menu_title()
    try:
        menu = int(input("메뉴를 선택하세요(1~6) => "))
        if menu < 1 or menu > 6:
          raise RightRangeError()
    except Exception as e:
        print("\n숫자를 입력하세요!!!(%s)\n" % e)
        continue

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
      print("\n프로그램 종료!!")
      break
    else:
      print("\n메뉴를 다시 입력하세요!!\n")
