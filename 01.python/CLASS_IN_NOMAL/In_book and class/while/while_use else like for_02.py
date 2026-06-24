i = 1 # 초기식
odd = 0
even = 0

while i <= 100: # 조건식
    if i % 2 == 0: # 반복 처리할 내용
        even += i
    else:
        odd += i
    i += 1 # 증감식
    if i > 100:
        break
else: # break의 아래에 있기 때문에 실행이 안된다.
    print("홀수의 합:", odd)
    print("짝수의 합:", even)