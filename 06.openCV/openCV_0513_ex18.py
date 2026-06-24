# 가우시안 블러링

import cv2

src = cv2.imread('./video/cat.jpg', cv2.IMREAD_COLOR)

# sigmaX : 가우시안  커널의 X축 방향 표준편차(Standard Deviation)을 의미
for ksize in (3, 5, 7, 11):
    dst = cv2.GaussianBlur(src, (ksize, ksize), 0)
    desc = 'Mean: {}x{}'.format(ksize, ksize)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()
cv2.destroyAllWindows()