# 자르기

import cv2

src = cv2.imread("./video/chess.jpg", cv2.IMREAD_COLOR)  # 체스 이미지, 컬러색상을 읽어올거임

dst = src.copy()                # 복사
roi = src[100:600, 200:700]     # 자르는 부분
dst[0:500, 0:500] = roi         # 자른걸 매칭시켜줌

src = cv2.resize(src, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)       # 사진크기를좀 줄여줌
dst = cv2.resize(dst, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)       # 사진크기를 좀 줄여줌
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()