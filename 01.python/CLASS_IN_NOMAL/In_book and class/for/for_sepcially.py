# 리스트 내포의 일반 문법
# 형식)[표현식 for 항목 in 반복가능객체 if 조건문]

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)