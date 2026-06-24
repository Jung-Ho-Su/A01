t1 = ()
print(type(t1))
t2 = (10,) # 값이 1개일 때 , 가 없으면 그냥 int가 되버리니 꼭 1개를 사용할 때는 , 를 사용하자
print(type(t2))
print(t2)
t3 = (1,2,3)
print(t3)
t4 = 1,2,3 # packing
print(t4)
x,y,z = t4 # unpacking 튜플로 만들어진 객체를 풀어주는 것
print(x,y,z)
t5 = (1, 10.5, "Python")
print(t5)
print(t5[2])
print(t5[2][0:2])
t5[2] = "Java" # 튜플은 값 변경X

a = [1,2,3,[4,5,6]]
a[3] : 100
print(a)
# 리스트 안의 리스트 전체는 변경부가능