# 확대 & 축소

import cv2

src = cv2.imread("./video/song_1.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

dst_pyrUp = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)

dst_pyrDown = cv2.pyrDown(src)

cv2.imshow("src", src)
cv2.imshow("pyrUp", dst_pyrUp)
cv2.imshow("pyrDown", dst_pyrDown)
cv2.waitKey()
cv2.destroyAllWindows()