import datetime
import cv2

capture = cv2.VideoCapture("./video/youquiz4.mp4")          # 동영상파일을 읽어와서
fourcc = cv2.VideoWriter_fourcc(*'XVID')                    # 코덱 형식 저장
record = False
while True:                                                 # 반복문
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):  # 현재 프레임 위치가 같은지 물어봄
        capture.open("./video/youquiz4.mp4")
    ret, frame = capture.read()                             # 한 프레임씩 읽어옴
    cv2.imshow("VideoFrame", frame)                 # 한 프레임씩 보여줌
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")   # 현재 시간을 ""형식으로 편집함
    key = cv2.waitKey(33)                                   # 키 입력을 기다림 만약 키 입력이 없으면 -1이 저장되어서
    print('key = >>', key)                                  # -1이 출력되면 키가 입력되지 않았다고 고려됨 // 만약 특정 키를 ㅇㅂ력하면 입력한 키 코드 값이 저장된다.

    if key == 27:                                           # 이스케이프에 대한 키 코드값이 27이다
        break
    elif key == 49:                                         # 숫자 1 에 대한 키 코드값
        print('캡쳐')
        cv2.imwrite("./capture" + str(now) + ".png", frame) # 읽어온 이미지의 프레임 정보를 언급된 위치에 현재 시간.png 저장 출력하겠다
    elif key == 50:                                         # 숫자 2 에 대한 키 코드값
        print("녹화 시작")
        record = True                                       # 녹화
        video = cv2.VideoWriter("./capture" + str(now) + ".avi", # 녹화하는 작업을 나타내는 코드
                                fourcc, 20.0, (frame.shape[1], frame.shape[0]))

    elif key == 51:                                         # 숫자 3 에 대한 키 코드값
        print("녹화 중지")
        record = False
        video.release()

    if record == True:
        print("녹화 중..")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()