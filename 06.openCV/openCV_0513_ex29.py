# 모폴로지 변환 예제_ex01
# 모폴로지(Morphological) 변환/연산
import cv2
import numpy as np

src = cv2.imread("./Video/zebra.jpg")

# 구조화 요소(커널 행렬)를 생성하는 함수
# shape: cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
print(kernel)

dilate = cv2.dilate(src, kernel, anchor=(-1, -1), iterations=5)
erode = cv2.erode(src, kernel, anchor=(-1, -1), iterations=5)

dst = np.concatenate((src, dilate, erode), axis=1)
dst_re = cv2.resize(dst, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()