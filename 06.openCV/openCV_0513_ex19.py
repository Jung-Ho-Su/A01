# 가장자리 검출 (Edge)

# 어느 방식이 절대적으로 경계선을 잘 나타내는 것은 아니고
# 이미지의 형태에 따라, 색상에 따라서 경계선을 잘 나타내는 것도 있고 아닌 것도 있다.

import cv2

src = cv2.imread("./video/wheat.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(laplacian, 50, 255)

sobel = cv2.resize(sobel, dsize=(600,400), interpolation=cv2.INTER_AREA)
laplacian = cv2.resize(laplacian, dsize=(600,400), interpolation=cv2.INTER_AREA)
canny = cv2.resize(canny, dsize=(600,400), interpolation=cv2.INTER_AREA)

cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()