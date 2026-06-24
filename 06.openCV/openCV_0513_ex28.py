# 기하학적변환(Geometric Perspective) 3
# 변환을 할 때 너비, 높이가 큰 값을 기준으로 변환된다.

import cv2
import numpy as np

win_name ='scanning'
img = cv2.imread('Video/paper.jpg')
src = cv2.resize(img, None, fx=2/3, fy=2/3, interpolation=cv2.INTER_AREA)
rows, cols = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)        # 4개의 좌표값을 저장하기 위한 배열

def onMouse(event, x, y, flags, param):
    global pts_cnt  # 좌표 개수를 카운트
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x, y]
        pts_cnt += 1
        if pts_cnt == 4:
            print(pts)
            sm = pts.sum(axis=1)
            diff = np.diff(pts, axis=1)
            print(diff)

            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]
            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

            w1 = abs(bottomRight[0] - bottomLeft[0])
            w2 = abs(topRight[0] - topLeft[0])
            h1 = abs(topRight[1] - bottomRight[1])
            h2 = abs(topLeft[1] - bottomLeft[1])
            width = int(max([w1, w2]))
            height = int(max([h1, h2]))
            pts2 = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1],
                               [0, height - 1]])

            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, mtrx, (width, height))
            cv2.imshow('scanned', result)

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 변환 작업은 여기까지