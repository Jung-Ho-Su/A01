import os
import cv2
from ultralytics import YOLO


def run_detection():
    # 1. 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 학습된 최신 가중치 파일 경로 (학습 시 설정한 project와 name 기준)
    # 만약 경로가 다르다면 직접 best.pt 파일의 경로를 입력하세요.
    weights_path = os.path.join(current_dir, 'runs', 'detect', 'ship_project', 'detect_scale_v1', 'weights', 'best.pt')

    if not os.path.exists(weights_path):
        print(f"❌ 가중치 파일을 찾을 수 없습니다: {weights_path}")
        return

    # 2. 모델 및 영상 로드
    model = YOLO(weights_path)
    video_path = os.path.join(current_dir, 'koko.mp4')
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"❌ 영상을 열 수 없습니다: {video_path}")
        return

    # 3. 영상 저장을 위한 설정 (선택 사항)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 탐지 결과가 포함된 영상을 'output_Miami_5.mp4'로 저장합니다.
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('koko.mp4', fourcc, fps, (w, h))

    print("\n--- [탐지 시작] 'q'를 누르면 중단됩니다 ---")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 4. YOLO 모델로 예측 (GPU 사용)
        # conf=0.25: 신뢰도가 25% 이상인 것만 표시
        # device=0: RTX 5060 GPU 사용
        results = model.predict(frame, conf=0.25, device=0, verbose=False)

        # 5. 결과 시각화
        annotated_frame = results[0].plot()  # 바운딩 박스와 라벨이 그려진 프레임

        # 화면 출력 및 파일 저장
        cv2.imshow("koko", annotated_frame)
        out.write(annotated_frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 6. 자원 해제
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("\n--- 탐지 완료 및 영상 저장 성공 (output_Miami_5.mp4) ---")


if __name__ == "__main__":
    run_detection()