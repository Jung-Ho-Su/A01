import os
import glob
import cv2
from ultralytics import YOLO

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 최신 학습 결과(best.pt) 탐색
search_pattern = os.path.join(current_dir, 'runs', 'detect', 'train*', 'weights', 'best.pt')
weights_list = glob.glob(search_pattern)

if weights_list:
    best_model_path = sorted(weights_list)[-1]
    print(f"✅ 사용 중인 모델: {best_model_path}")
    model = YOLO(best_model_path)

    # 3. 분석 대상 영상 설정: 항구안큰바다(만).mp4
    video_name = '항구안큰바다(만).mp4'
    video_path = os.path.join(current_dir, video_name)

    if os.path.exists(video_path):
        cap = cv2.VideoCapture(video_path)

        # 결과 저장을 위한 설정 (필요 시 사용)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        print(f"--- '{video_name}' 분석을 시작합니다 (종료: 'q') ---")

        while cap.isOpened():
            success, frame = cap.read()
            if not success: break

            # [해결책] 인식률이 낮을 때 적용하는 정밀 추론 설정
            # 1. imgsz=1280: 멀리 있는 작은 배를 잡기 위해 해상도를 높여서 추론 (RTX 5060이라 속도 충분함)
            # 2. conf=0.25: 현재 인식률이 0.34 정도로 낮으므로, 일단 0.25로 낮춰서 더 많이 탐지하게 함
            # 3. augment=True: 추론 시 성능을 조금 더 끌어올리는 기법 (TTA)
            results = model.predict(
                frame,
                conf=0.25,
                imgsz=1280,
                device=0,  # GPU 사용
                augment=True,
                verbose=False
            )

            # 결과 시각화
            annotated_frame = results[0].plot()

            # 화면에 현재 인식 정보 표시 (디버깅용)
            cv2.putText(annotated_frame, f"Analyzing: {video_name}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Marine Surveillance - Port Analysis", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        print(f"❌ 영상 파일을 찾을 수 없습니다: {video_path}\n파일명과 경로를 확인하세요.")
else:
    print("❌ 학습된 모델을 찾을 수 없습니다.")