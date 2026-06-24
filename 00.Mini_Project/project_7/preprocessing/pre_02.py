import os
import glob
import cv2
from ultralytics import YOLO

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 가장 최신 학습 결과(best.pt) 자동 탐색
# 만약 특정 위치의 모델을 쓰고 싶다면 직접 경로를 적으셔도 됩니다. (예: best_model_path = 'runs/detect/train1/weights/best.pt')
search_pattern = os.path.join(current_dir, 'runs', 'detect', 'train*', 'weights', 'best.pt')
weights_list = glob.glob(search_pattern)

if weights_list:
    # 가장 최근에 생성된(마지막 순서) 모델 선택
    best_model_path = sorted(weights_list)[-1]
    print(f"✅ 사용 중인 모델: {best_model_path}")

    # 모델 로드
    model = YOLO(best_model_path)

    # 3. 영상 파일 확인
    video_path = os.path.join(current_dir, 'ship_video_01.mp4')

    if os.path.exists(video_path):
        cap = cv2.VideoCapture(video_path)

        # 영상의 원래 해상도나 FPS 정보를 가져올 수 있습니다.
        print("--- 영상 재생을 시작합니다. (종료하려면 영상 창에서 'q'를 누르세요) ---")

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("영상 재생이 완료되었습니다.")
                break

            # 모델 추론 (stream=True로 메모리 효율 최적화)
            # conf: 0.3 (30% 확률 이상만 표시), imgsz: 학습 때와 동일하게 640
            results = model.predict(frame, conf=0.3, imgsz=640, verbose=False)

            # 결과 시각화 (바운딩 박스 등이 그려진 프레임)
            annotated_frame = results[0].plot()

            # 화면 출력
            cv2.imshow("Ship Detection Inference", annotated_frame)

            # 'q' 키를 누르면 즉시 종료
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        print(f"❌ 영상 파일을 찾을 수 없습니다: {video_path}")
else:
    print("❌ 학습된 모델(best.pt)을 찾을 수 없습니다. 먼저 학습을 완료해주세요.")

    # 학습을 해서 ship_video_01을 영상 틀었지만 object로만 배를 인식하고 인식률도 0.34로 낮은편