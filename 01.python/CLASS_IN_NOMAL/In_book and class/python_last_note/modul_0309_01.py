# datetime.data() : 연, 월, 일로 날짜를 표현할 때 사용하는 함수
import datetime

day =datetime.date(2021,12,14)
print(day)
print(day.weekday())

# time.time() : UTC(universal time coordinated, 협정 세계 표준시)를 사용하여 현재 시간을
# 실수 형태로 반환하는 함수
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환
import time
print(time.time())

# time.localtime() : time.time()이 반환한 실숫값을 연, 월, 일, 시, 분, 초 ...
# 형태로 바꾸어 주는 함수
print(time.localtime(time.time()))
