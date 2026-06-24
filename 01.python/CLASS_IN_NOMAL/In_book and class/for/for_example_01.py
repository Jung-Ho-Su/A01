message = "Hello!"
messages = ["Hello World", "강릉원주대학교 정보기술공학과"]
numbers = (1,2,3)
polygon = {"triangle":2, "rectangle":1, "line":0} # 비순서
color = {"red", "green", "blue"} #set 객체 # 비순서
for item in message:
    print(item)
print('1.---------------------')
for item in messages:
    print(item)
print('2.---------------------')
for item in numbers:
    print(item)
print('3.---------------------')
for item in polygon:
    print(item)
for item in polygon:
    print(polygon[item])
for item in polygon:
    print(polygon.get(item))
print('4.---------------------')
for item in color:
    print(item)