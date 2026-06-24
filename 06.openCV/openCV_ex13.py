#역상

# 비전처리에서 이미지를 다룰 때 역상으로 다루는 경우가 더 좋은 경우가 있기 때문에 이를
# 판별하는데 활용하는 것이 좋다
# 왜냐 경계선이 잘 보이기 때문에 역상이미지를 주면 경계선이 잘 보여서 활용하기 좋다.

import cv2

src = cv2.imread("./video/bird.jpg", cv2.IMREAD_COLOR)
dst = cv2.bitwise_not(src)

src = cv2.resize(src, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)
dst = cv2.resize(dst, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()