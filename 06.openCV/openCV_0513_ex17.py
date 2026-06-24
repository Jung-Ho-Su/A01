# 흐림효과
import cv2

src = cv2.imread('./video/cat.jpg', cv2.IMREAD_COLOR)
dst = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 커널 사이즈 다르게 해보기
for ksize in (3, 5, 7, 11):
    dst = cv2.blur(src, (ksize, ksize), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
    desc = 'Mean: {}x{}'.format(ksize, ksize)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()
cv2.destroyAllWindows()