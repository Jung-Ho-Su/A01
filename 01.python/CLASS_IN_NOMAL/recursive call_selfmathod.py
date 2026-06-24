#재귀 함수
# def factorial(n):
#     result = 1
#     for i in range(n, 0, -1):
#         result *= i
#     return result
# print(factorial(5))

def fatorial(n):
    if n == 1: # n이 1일 때
        return 1 #1을 반환하고 재귀호출을 끝냄
    return n * fatorial(n - 1) # n과 factorial 함수에 n-1을 넣어서 변환됨
print(fatorial(5))
