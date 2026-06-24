def add(a, *b, **c): # **b : 정의되지 않은 매개변수
    hap = a
    for val in b:
        hap += val
    for val in c:
        hap += c[val]
    return hap

print(add(10, 20, 30, mbc=40, kbs=50)) #함수 호출문
print(add(10, 20, 30, 40, one=50, two=60, three=70)) # 함수 호출문