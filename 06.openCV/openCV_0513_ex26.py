# 기하학적변환(Geometric Perspective)
# 첫번째 예제

import cv2
import numpy as np

src = cv2.imread('./Video/harvest.jpg', cv2.IMREAD_COLOR)
height, width, channels = src.shape

srcPoint = np.array([[300, 200], [400, 200], [500, 500], [200, 500]], # 이미지에서 점 4개의 좌표를 찍어서 여기에 있는 원본 이미지에서 4개의 위치를 정해서 배열을 만들어서 구역을 정함
                    dtype=np.float32)
dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], # 위에서 부분적으로 짤린 이미지를 4개의 정규화된 목적 위치를 지정해줘서 정규화해준다.
                    dtype=np.float32)

matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)        # 변환 행렬이 여기서 만들어짐
dst = cv2.warpPerspective(src, matrix, (width, height))     # 앞서 만들어진 변환 행렬을 이용해서 여기서 실제적인 변환을 실행한다.

src = cv2.resize(src, dsize=(800, 600), interpolation=cv2.INTER_AREA)
dst = cv2.resize(dst, dsize=(800, 600), interpolation=cv2.INTER_AREA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()