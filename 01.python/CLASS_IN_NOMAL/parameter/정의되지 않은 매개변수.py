def add(a, **b): # **b : 정의되지 않은 매개변수
    hap = a
    for val in b:
        hap += b[val]
    return hap

print(add(10, mbc=20, kbs=30)) #함수 호출문, 키워드 매개변수를 인자로 전달
print(add(10, one=20, two=30, three=40)) # 함수 호출문