# 이진화 예제 2 // origin 하고 나머지 비교해 볼 수 있는 예제
# 이 작업 할 때는 단색으로 변환시켜 줘야하기 때문에 첫번째로 cv2.imread_grayscale 이라고 해서 단색으로 바꿔준다.
#

import cv2
import matplotlib.pyplot as plt

# img = cv2.imread("video/gray_gradient.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("video/chess.jpg", cv2.IMREAD_GRAYSCALE)


_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

imgs = {'origin': img, 'BINARY': t_2zr, 'BINARY_INV': t_bininv,
        'TRUC': t_truc, 'TOZERO': t_2zr, 'TOZERO_INV': t_2zrinv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()