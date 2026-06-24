# HSV(색상 Hue, 채도 Saturation, 명도 Value) 2
# 원하는 색상의 토마토를 출력하는 예제

import cv2

src = cv2.imread('./Video/tomato.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv) # 색상값을 잡아줌

h = cv2.inRange(h, 8, 20) # inrange(src,lowerb,upperb)
orange = cv2.bitwise_and(hsv, hsv, mask = h) # bit단위로 and 연산을 하겠다는 의미
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)

src = cv2.resize(src, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)
orange = cv2.resize(orange, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)

cv2.imshow('src', src)
cv2.imshow('orange', orange)
cv2.waitKey()
cv2.destroyAllWindows()