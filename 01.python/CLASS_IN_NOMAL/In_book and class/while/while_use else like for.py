i = 1 # 초기식
odd = 0
even = 0

while i <= 100: # 조건식
    if i % 2 == 0: # 반복 처리할 내용
        even += i
    else:
        odd += i
    i += 1 # 증감식
else: # for문의 else와 while 문의 else는 같다
    print("홀수의 합:", odd)
    print("짝수의 합:", even)