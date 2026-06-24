# 모폴로지 변환 예제_ex02
# 모폴로지(Morphological) 변환/연산
# 커널 유형에 따라서 팽창 유형에 따라 설명
# 효과를 보고 침식과 팽창 어떤걸 사용할지는 정하면 된다.

import cv2
import numpy as np

img = cv2.imread("video/morph_hole.png")

k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
k2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

rect = cv2.dilate(img, k1, iterations=3)
cross = cv2.dilate(img, k2, iterations=3)
ellipse = cv2.dilate(img, k3, iterations=3)

merged = np.hstack((img, rect, cross, ellipse))
cv2.imshow("Dilation", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()