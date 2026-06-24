total = 0

for item in range(1, 101, 1):
    total = total + item
else: # for 문의 else는 이전의 for문을 정상적으로 완료하고 뒤에 else를 실행한다.
    print("1부터 10까지 합은", total, "입니다.")

# 만약 for 문이 정상적으로 시행되지 않으면, else는 시행되지 않는다.
# 즉 for 문이 정상적으로 실행 되었을 경우에만 뒤에 for 문과 동등한 else가 시행된다.