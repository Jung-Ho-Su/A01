# #1에서부터 100까지 숫자 중 홀수의 합과 짝수의 합을 구해서 출력하시오.
#
hole = 0
zzak = 0
i = 1

while i in range(1, 101):
    if (i % 2) == 0:
        zzak = zzak + i
    else:
        hole = hole + i
    i += 1

print(zzak)
print(hole)

# i = 1 # 초기식
# odd = 0
# even = 0
#
# while i <= 100: # 조건식
#     if i % 2 == 0: # 반복 처리할 내용
#         even += i
#     else:
#         odd += i
#     i += 1 # 증감식
# print("홀수의 합:", odd)
# print("짝수의 합:", even)