# with open('hello.txt', 'rt') as file:
#     s = file.read()
#     print(s)

with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write("hello world! {0}\n".format(i))

#format 함수는 {} 안에 변수를 할당해주는 역할