# 이미지 다루는 예제

import cv2

image = cv2.imread("./video/cat.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()