lst = []

while True:
    dct = {}
    dct['학번']= input("학번을 입력하시오.")
    if dct['학번'].lower() == 'exit':
        break
    dct['이름'] = input("이름을 입력하시오.")
    dct['국어'] = int(input("국어점수를 입력하시오."))
    dct['영어'] = int(input("영어점수를 입력하시오."))
    dct['수학'] = int(input("수학점수를 입력하시오."))

    dct['총점'] = (dct['국어']+dct['영어']+dct['수학'])
    dct['평균'] = dct['총점']/3

    lst.append(dct)
    print()


print("\t\t***성적표***")
print("================================")
print("학번 이름 국어 영어 수학 총점 평균")
total = 0
for dct in lst:
    total += dct['평균']
    avg_total = total / len(lst)
    print("%s %3s %1d %2d %3d %3d %5.2f" %
          (dct['학번'], dct['이름'], dct['국어'], dct['영어'], dct['수학'], dct['총점'], dct['평균']))
print("================================")
print("\t학생수:%d" % len(lst), "\t전체 평균:%5.2f" % avg_total)
