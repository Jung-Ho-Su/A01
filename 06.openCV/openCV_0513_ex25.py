# 도형 그리기
# selectROI # 2

import cv2

img = cv2.imread('./Video/sunset.jpg')
x, y, w, h = cv2.selectROI('img', img, False)
print(x, y, w, h)
if w and h:
    roi = img[y:y + h, x:x + w]
    cv2.imshow('corpped', roi)
    cv2.moveWindow('corpped', 0, 0)
    cv2.imwrite('./Video/cropped2111.jpg', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()