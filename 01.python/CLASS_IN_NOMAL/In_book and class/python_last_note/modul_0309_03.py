# datetime 클래스 : 날짜와 시간을 동시에 표현하기 위해서 사용되며 위에서
#     다룬 date와 time 클래스에서 지원하는 대부분의 기능을 지원

from datetime import datetime

now = datetime.now()
print("현재 날짜와 시간:", now)
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("포멧된 날짜와 시간:", formatted_date)
print("%s년 %s월 %s일 %s시 %s분 %s초" % (now.year, now.month, now.day, now.hour, now.minute, now.second))

print(datetime(2026,3,8,10,10,10))
print(datetime(2026,3,8))

# random 모듈 : 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
# random() 함수 : 0부터 1사이의 랜덤 실수를 반환한다.
# uniform() 함수 : 2개의 숫자 사이의 랜덤 실수를 반환한다.
# randint() 함수 : 2개의 숫자 사이의 랜덤 정수를 반환한다.
#                 (2번째 인자로 넘어온 정수도 범위에 포함시킴)
# choice() 함수 : 랜덤하게 하나의 원소를 선택한다.
# sample() 함수 : 랜덤하게 여러 개의 원소를 선택한다.
# shuffle() 함수 : 원소의 순서를 랜덤하게 변경한다.
import random

print(random.random()) # 0과 1사이 난수 생성
print('1.--------------------------------------')
print(random.uniform(1, 10)) # 1과 10 사이의 난수 생성
print('2.--------------------------------------')
print(random.randint(1, 10)) # 1부터 10사이의 정수형 난수 반환
print('3.--------------------------------------')
print(random.randrange(0, 100,2)) # 0부터 100사이 짝수중 (2증가) 하나 선택
print('4.--------------------------------------')
print(random.choice('abcdefghij')) # 작성한 값 중 하나 선택 후 반환
print('5.--------------------------------------')
print(random.sample([1,2,3,4,5], 3)) # k개의 인덱스를 임의로 선택해서 반환
print('6.--------------------------------------')
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items) # 해당 인덱스의 순서를 임의로 바꾼 후 반환
print(items)
