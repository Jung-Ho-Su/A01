# 이진화

import cv2

src = cv2.imread("./video/duck.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) # THRESH_BINARY : 이걸 사용해서 어떤 함수가 이미지를 찾고자 할 때 잘 탐색할 수 있는지 확인하기

gray = cv2.resize(gray, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
src = cv2.resize(src, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
dst = cv2.resize(dst, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("gray", gray)
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()