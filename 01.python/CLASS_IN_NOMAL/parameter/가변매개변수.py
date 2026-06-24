def add(a, *b): # *b : 가변 매개변수
    hap = a
    for val in b:
        hap += val
    return hap

print(add(10, 20, 30)) # 함수 호출문
print(add(10, 10, 20, 30)) # 함수 호출문