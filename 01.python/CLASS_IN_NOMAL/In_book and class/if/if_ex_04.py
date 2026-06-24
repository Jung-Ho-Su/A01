score = int(input("총점을 입력해 주세요"))

if score >= 90:
    print("수")
elif 80 <= score <= 90:
    print("우")
elif 70 <= score <= 80:
    print("미")
elif 60 <= score <= 70:
    print("양")
else:
    print("가")