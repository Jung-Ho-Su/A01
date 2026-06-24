import cv2
import matplotlib.pyplot as plt

def img_show(title='image', img=None, figsize=(8, 5)): # img_show :이미지 출력을 위한함수
    plt.figure(figsize=figsize)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []

            for i in range(len(img)):
                titles.append(title)

        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        if len(img.shape) <= 3: # 이미지가 단색이라는 의미
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()

src = cv2.imread("./Video/cat.jpg", cv2.IMREAD_COLOR) # 이미지를 읽어옴
height, width, channels = src.shape
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
print(matrix)   # 맵 아핀 행렬 # getRotationMatrix2D 얘가 맵 아핀 행렬을 만들어줌
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imshow("src", src)
cv2.imshow("dst", dst)
img_show(["Original", "ritate_90"], [src, dst])
cv2.waitKey()
cv2.destroyAllWindows()