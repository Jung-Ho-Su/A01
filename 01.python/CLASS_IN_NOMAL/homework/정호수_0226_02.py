lst = []

while True:
    lt = []
    lt.append(input("학번을 입력하시오.")) # 0
    if 'exit' in lt:
        break
    lt.append(input("이름을 입력하시오.")) # 1
    lt.append(int(input("국어을 입력하시오."))) # 2
    lt.append(int(input("영어을 입력하시오."))) # 3
    lt.append(int(input("수학을 입력하시오."))) # 4

    lt.append(lt[2]+lt[3]+lt[4]) # 총점 # 5
    lt.append(lt[5]/3) # 평균 # 6
    lst.append(lt)
    print()


print("\t\t***성적표***")
print("================================")
print("학번 이름 국어 영어 수학 총점 평균")

total = 0
for lt in lst:
    total += lt[5]
    avg_total = total / len(lst)
    print("%s %3s %1d %2d %3d %3d %5.2f" %
          (lt[0], lt[1], lt[2], lt[3], lt[4], lt[5], lt[6]))

print("================================")
print("\t학생수:%d" % len(lst), "\t전체 평균:%5.2f" % avg_total)
