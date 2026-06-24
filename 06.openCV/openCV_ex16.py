# 적응형 이진화

import cv2
import matplotlib.pyplot as plt

blk_size = 9
C = 5
img = cv2.imread('video/sudoku.png', cv2.IMREAD_GRAYSCALE)
# 오츠 알고리즘을 사용하여 임계값을 자동으로 설정
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY_INV, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY_INV, blk_size, C)

imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1,
        'Adapted-Mean':th2, 'Adapted-Gaussian': th3}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.title(key)
    plt.imshow(value, 'gray')
    plt.xticks([]), plt.yticks([])

plt.show()