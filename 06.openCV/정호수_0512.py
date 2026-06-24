import cv2
from ultralytics import YOLO

# [처리조건 1] 카메라로 촬영한 영상을 yolo26.avi라는 이름으로 저장
def record_video():
    cap = cv2.VideoCapture(0)                   # 노트북 웹캠 연결

    # XVID : 호환성이 좋은 avi , DIVX : XVID에 사용하며 고화질영상에 사용함,
    fourcc = cv2.VideoWriter_fourcc(*'XVID')    # 코덱 : 영상 오디오를 압축하고 푸는 기술
    fps = 20.0                                  # 프레임 : 20으로 설정
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))      # 가로값을 넓이로
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))    # 세로값을 높이로
    out = cv2.VideoWriter('yolo26.avi', fourcc, fps, (width, height))   # 설정된 값으로 'yolo26.avi' 영상 생성

    while True:
        ret, frame = cap.read() # ret : 영상을 성공적으로 읽어왔는지 알려주는 상태 신호 // # frame : 이미지 데이터 담김
        if not ret:
            break

        out.write(frame)                        # 읽어온 프레임을 비디오 파일에 저장
        if cv2.waitKey(1) & 0xFF == ord('q'):   # 1ms 동안 키 입력을 대기하며, 누른 키가 'q'이면 종료
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("영상 저장 완료: yolo26.avi")


# [처리조건 2] 저장된 영상을 불러와 YOLO 모델로 객체 탐지 수행
def detect_objects():
    model = YOLO("yolo26n.pt")

    cap = cv2.VideoCapture('yolo26.avi')

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, conf=0.5)                # 현재 프레임에서 신뢰도 50% 이상의 객체만 탐지

        for result in results:
            boxes = result.boxes                        # 결과에서 박스 정보(좌표, 신뢰도, 클래스) 추출
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # 좌상단(x1, y1)과 우하단(x2, y2) 좌표를 정수로 변환
                conf = box.conf[0].item()               # 해당 객체일 확률(신뢰도) 값을 가져옴
                cls_id = int(box.cls[0].item())         # 탐지된 클래스의 고유 번호(ID)를 가져옴
                label = model.names[cls_id]             # 모델의 클래스 이름 명단에서 ID에 해당하는 이름 매칭

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)    # 객체 주위에 빨간색(BGR) 박스 그리기
                text = f"{label} {conf:.2f}"                                # 레이블 이름과 신뢰도를 소수점 둘째 자리까지 문자열로 포맷
                cv2.putText(frame, text, (x1, y1 - 10),                 # 박스 위에 텍스트 표시
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        if cv2.waitKey(30) & 0xFF == ord('q'):          # 약 30ms 대기(초당 약 33프레임 속도)하며 'q' 입력 시 종료
            break

    cap.release()
    cv2.destroyAllWindows()
    print("종료")


if __name__ == "__main__":
    record_video()  # 영상 촬영 및 저장
    detect_objects()  # 저장된 영상으로 객체 탐지