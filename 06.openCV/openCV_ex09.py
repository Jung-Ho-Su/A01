# 확대 & 축소 2

import cv2
import numpy as np

img = cv2.imread("./video/cat.jpg") # 원본이미지
smaller = cv2.pyrDown(img)          # 축소
bigger = cv2.pyrUp(smaller)         # 확대

laplacian = cv2.subtract(img, bigger)   # 라플라시안 값에 대해서
restored = bigger + laplacian           # 원본이미지를 복원함 # 해상도가 달라짐!!

# merged = np.hstack((img, laplacian, bigger, restored))
# cv2.imshow('Laplacian Pyramid', merged)
cv2.imshow('img', img)
cv2.imshow('bigger', bigger)
cv2.imshow('restored', restored)
cv2.waitKey(0)
cv2.destroyAllWindows()