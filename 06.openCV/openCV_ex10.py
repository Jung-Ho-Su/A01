# 크기 조절

import cv2

src = cv2.imread("./video/cat.jpg", cv2.IMREAD_COLOR)

dst = cv2.resize(src, dsize=(800, 600), interpolation=cv2.INTER_AREA) # INTER_AREA 이거는 바꿔가면서 비교하면 확인해보기
dst2 = cv2.resize(src,dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()