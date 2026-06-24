# 비디오 출력 예제
# 무한 재생하는 예제

import cv2

capture = cv2.VideoCapture("./video/youquiz4.mp4")
print(capture.get(cv2.CAP_PROP_POS_FRAMES))             # 현재 프레임 위치
print(capture.get(cv2.CAP_PROP_FRAME_COUNT))            # 총 프레임 개수
while cv2.waitKey(33) < 0:                               # 키 입력을 안하면 -1을 반환시켜줘 true가 된다.
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT): # 프레임이 끝에 도달하게 되면
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)     # 다시 0으로 반환해서 다시 시작하도록 한다,

    ret, frame = capture.read()
    cv2.imshow('wildlife', frame)

capture.release()
cv2.destroyAllWindows()