# 모폴로지 변환 예제_ex05
# 모폴로지(Morphological) 변환/연산
# 그레디언트 = 팽창 - 침식

import cv2
import numpy as np

img = cv2.imread("video/morphological.png")
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
merged = np.hstack((img, gradient))
cv2.imshow("Gradient", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()