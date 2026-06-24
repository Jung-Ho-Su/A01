# time.strftime() : 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
import time
## strftime 에서 f 는 format /str 은 string / time 은 시간
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))










