import cv2

print(cv2.__version__)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while cv2.waitKey(33) < 0: # 밀리초세컨드 33초 0.033초 동안 응답이 없으면 -1을 반환시켜준다. // key입력이 없는 경우에는
    ret, frame = capture.read()
    cv2.imshow('VideoFrame',frame)

capture.release()
cv2.destroyAllWindows()

# 카메라 켜야함...?