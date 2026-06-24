# 모폴로지 변환 예제_ex06
# 모폴로지(Morphological) 변환/연산
# 탑햇 (Tophat) = src - open
# 블랙햇 (Blackhat) = close - src

import cv2
import numpy as np

img = cv2.imread('video/moon_gray.jpg')
k = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)
merged = np.hstack((img, tophat, blackhat))
cv2.imshow('tophat blackhat', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()