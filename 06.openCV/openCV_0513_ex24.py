# 도형 그리기
# selectROI

import cv2

isDragging = False                  # 드래그 유무 상태를 나타내는 값
x0, y0, w, h = -1,-1,-1,-1
blue, red = (255,0,0),(0,0,255)     # 색상값을 blue, red에 각각 저장하고 있다. openCV는 순서가 bgr이다

def onMouse(event,x,y,flags,param): # 발생한 이벤트에 관한 객체정보를 event가 전달받는다
    global isDragging, x0, y0, isDragging
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스L버튼에 대해서 이벤트가 발생할 때
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스가 움직이는 이벤트가 발생했을 때
        if isDragging:                  # isDragging 이 true 인지 확인
            img_draw = img.copy()       # 드래그 값을복사하고
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)  # 드래그가 사각형을 그린다
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:  # 버튼을 누르고 난 다음에 다시 올라오는 이벤트가 발생했을 떄
        if isDragging:                  # 드래그 중지
            isDragging = False
            w = x - x0
            h = y - y0
            print("x:%d, y:%d, w:%d, h:%d" % (x0,y0,w,h))
            if w > 0 and h > 0:
                img_draw = img.copy()
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw)
                roi = img[y0:y0 + h, x0:x0 + w] # 내가 관심있는 영역을 표시해서 오류를 roi 변수에 저장하겠다는 의미
                cv2.imshow('cropped', roi)
                cv2.moveWindow('cropped', 0, 0)
                cv2.imwrite("./video/cropped.jpg", roi)
                print("croped.")
            else:
                cv2.imshow('img', img)
                print("좌측 상단에서 우측 하단으로 영역을 드래그 하세요.")

img = cv2.imread('./video/sunset.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse) # setMouseCallbak() : 마우스와 관련된 이벤트가 발생하면 함수를 호출하라는 함수로 여기서는 onMouse의 함수를 호출하겠다는 뜻
cv2.waitKey()
cv2.destroyAllWindows()