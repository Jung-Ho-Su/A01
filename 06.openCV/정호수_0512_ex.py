import cv2  # OpenCV 라이브러리 임포트 (영상 처리 및 출력)
from ultralytics import YOLO  # Ultralytics의 YOLO 라이브러리 임포트 (딥러닝 모델 사용)

# [처리조건 1] 카메라로 촬영한 영상을 yolo26.avi라는 이름으로 저장
def record_video():
    cap = cv2.VideoCapture(0)  # 노트북의 기본 웹캠(인덱스 0) 장치와 연결

    # 영상 저장을 위한 설정 (코덱, FPS, 해상도)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # AVI 형식에 주로 사용되는 XVID 비디오 코덱 설정
    fps = 20.0  # 초당 프레임 수(FPS)를 20으로 설정
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 카메라 장치의 가로 해상도 값을 정수형으로 가져옴
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 카메라 장치의 세로 해상도 값을 정수형으로 가져옴

    out = cv2.VideoWriter('yolo26.avi', fourcc, fps, (width, height))  # 설정한 옵션으로 'yolo26.avi' 파일 쓰기 객체 생성

    print("녹화를 시작합니다. 'q'를 누르면 녹화가 종료됩니다.")  # 사용자에게 시작 알림 출력

    while cap.isOpened():  # 카메라 장치가 정상적으로 열려 있는 동안 반복
        ret, frame = cap.read()  # 카메라로부터 한 프레임의 영상을 읽어옴 (ret: 성공여부, frame: 이미지 데이터)
        if not ret:  # 영상을 읽어오지 못했을 경우 (에러 등)
            break  # 반복문 종료

        out.write(frame)  # 읽어온 프레임을 비디오 파일에 저장
        cv2.imshow('Recording...', frame)  # 'Recording...'이라는 창에 실시간 영상 표시

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 1ms 동안 키 입력을 대기하며, 누른 키가 'q'이면
            break  # 반복문 종료

    cap.release()  # 카메라 장치 자원 해제
    out.release()  # 비디오 쓰기 객체 자원 해제 (파일 닫기)
    cv2.destroyAllWindows()  # 생성된 모든 OpenCV 창 닫기
    print("영상 저장 완료: yolo26.avi")  # 저장 완료 메시지 출력


# [처리조건 2] 저장된 영상을 불러와 YOLO 모델로 객체 탐지 수행
def detect_objects():
    # 현재 환경에서 사용 가능한 최신 YOLO 모델 로드 (yolo26n-cls가 아닌 Detection 모델 사용)
    # 과제에서 명시한 'yolo26'의 의미를 살려 최신 가중치 파일을 로드합니다.
    model = YOLO("yolo26n.pt")  # YOLOv11 nano 모델 가중치 파일을 로드 (객체 탐지용)

    cap = cv2.VideoCapture('yolo26.avi')  # 위에서 저장한 'yolo26.avi' 비디오 파일 불러오기

    while cap.isOpened():  # 비디오 파일이 정상적으로 열려 있는 동안 반복
        ret, frame = cap.read()  # 비디오 파일에서 한 프레임을 읽어옴
        if not ret:  # 비디오 끝에 도달하거나 프레임 읽기에 실패하면
            break  # 반복문 종료

        # YOLO 모델로 객체 탐지 수행 (conf=0.5 설정)
        results = model(frame, conf=0.5)  # 현재 프레임에서 신뢰도 50% 이상의 객체만 탐지

        # 탐지된 객체 정보 추출 및 시각화
        for result in results:  # 탐지 결과 리스트를 순회
            boxes = result.boxes  # 결과에서 박스 정보(좌표, 신뢰도, 클래스) 추출
            for box in boxes:  # 탐지된 각 객체 박스마다 반복
                # 바운딩 박스 좌표
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # 좌상단(x1, y1)과 우하단(x2, y2) 좌표를 정수로 변환
                # 신뢰도 (confidence)
                conf = box.conf[0].item()  # 해당 객체일 확률(신뢰도) 값을 가져옴
                # 클래스 이름
                cls_id = int(box.cls[0].item())  # 탐지된 클래스의 고유 번호(ID)를 가져옴
                label = model.names[cls_id]  # 모델의 클래스 이름 명단에서 ID에 해당하는 이름 매칭

                # 영상에 바운딩 박스 및 텍스트 출력
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 객체 주위에 빨간색(BGR) 박스 그리기
                text = f"{label} {conf:.2f}"  # 레이블 이름과 신뢰도를 소수점 둘째 자리까지 문자열로 포맷
                cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)  # 박스 위에 텍스트 표시

        cv2.imshow('YOLO Object Detection', frame)  # 탐지 결과가 그려진 프레임을 화면에 출력

        if cv2.waitKey(30) & 0xFF == ord('q'):  # 약 30ms 대기(초당 약 33프레임 속도)하며 'q' 입력 시 종료
            break  # 반복문 종료

    cap.release()  # 비디오 파일 자원 해제
    cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기
    print("탐지 프로그램 종료")  # 종료 메시지 출력


if __name__ == "__main__":  # 스크립트가 직접 실행될 경우
    record_video()  # 영상 촬영 및 저장 함수 호출
    detect_objects()  # 저장된 영상으로 객체 탐지 함수 호출