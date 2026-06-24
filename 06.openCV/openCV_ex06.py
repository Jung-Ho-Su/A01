# 대칭(Filp)

import cv2

src = cv2.imread("./Video/cat.jpg", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)
dst1 = cv2.flip(src, 1)
dat2 = cv2.flip(src, -1)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst)
cv2.waitKey()
cv2.destroyAllWindows()