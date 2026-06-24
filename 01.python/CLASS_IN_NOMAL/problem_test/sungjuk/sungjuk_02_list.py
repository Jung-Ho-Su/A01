ls = []
ls.append(input("학번을 입력하시오")) #0
ls.append(input("이름을 입력하시오")) #1
ls.append(int(input("국어 점수를 입력하시오."))) #2
ls.append(int(input("영어 점수를 입력하시오."))) #3
ls.append(int(input("수학 점수를 입력하시오."))) #4

ls.append((ls[2]+ls[3]+ls[4])) #5
ls.append((ls[2]+ls[3]+ls[4])/3) #6

print("            ***성적표***              ")
print("====================================")
print("학번 이름 국어 영어 수학 총점 평균")
print("====================================")
print("%s %3s %2d %2d %2d %4d %2.2f" % (ls[0], ls[1], ls[2], ls[3], ls[4], ls[5], ls[6]))
print("====================================")