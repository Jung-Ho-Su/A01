hak = input("학번을 입력하시오")
name = input("이름을 입력하시오")
la = int(input("국어 점수를 입력하시오."))
en = int(input("영어 점수를 입력하시오."))
ma = int(input("수학 점수를 입력하시오."))

total = la + en + ma
agv = round(((la + en + ma) / 3), 2)

print("            ***성적표***              ")
print("====================================")
print("학번 이름 국어 영어 수학 총점 평균")
print("====================================")
print("%s %3s %2d %2d %2d %4d %2.2f" % (hak, name, la, en, ma, total, agv))
print("====================================")