# 웹캠으로 찍은 내용을 저장하는 내용

import cv2

cap = cv2.VideoCapture(0)                                   # 카메라를 여는 작업
if cap.isOpened:
    file_path = 'video/record.avi'                          # 비디오애 '' 안의 이름으로 저장
    fps = 30.0                                              # 30 프레임으로 저장
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)               # get() : 속성값을 읽어올 때 사용하느 코드
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))                        # 튜플형식으로 size에 저장
    out = cv2.VideoWriter(file_path, fourcc, fps, size)     # 튜플형태로 출력 객체를 하나 만듦
    while True:
        ret, frame = cap.read()                             # 카메라로부터 화면을 읽어옴 ret, 반환객체
        if ret:
            cv2.imshow('camera-recording', frame)   # 화면출력
            out.write(frame)                                # 파일 출력
            if cv2.waitKey(int(1000 / fps)) != -1:          # ????????????????????????????????????????
                break

        else:
            print("no frame !")
            break
    out.release()

else:
    print("can't open camera!")
cap.release()
cv2.destroyAllWindows()