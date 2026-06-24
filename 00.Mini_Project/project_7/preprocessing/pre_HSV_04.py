import os
import cv2
import glob
from ultralytics import YOLO

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 가장 최근에 학습된 best.pt 모델 찾기
# 'runs/detect/train*/weights/best.pt' 경로에서 가장 마지막 파일을 가져옵니다.
weights_pattern = os.path.join(current_dir, 'runs', 'detect', 'train*', 'weights', 'best.pt')
best_weights_list = sorted(glob.glob(weights_pattern))

if not best_weights_list:
    print("❌ 학습된 모델(best.pt)을 찾을 수 없습니다. 경로를 확인해주세요.")
    exit()

best_weights = best_weights_list[-1]  # 가장 최근 학습 결과 선택
print(f"✅ 사용 모델: {best_weights}")

# 3. 모델 로드
model = YOLO(best_weights)

# 4. 영상 소스 설정 (동영상 파일 또는 웹캠)
# 동영상 파일일 경우 파일명을, 웹캠일 경우 0을 입력하세요.
video_path = os.path.join(current_dir, 'ship_video_01.mp4')
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ 영상을 열 수 없습니다. 경로를 확인하거나 카메라 연결을 확인하세요.")
    exit()

print("\n--- [테스트] 실시간 영상 감지를 시작합니다. 'q'를 누르면 종료됩니다. ---")

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("영상 재생이 완료되었거나 중단되었습니다.")
        break

    # 5. YOLO 예측 수행
    # conf=0.3: 신뢰도 30% 이상인 객체만 표시
    # iou=0.45: 박스가 겹칠 때 중복 제거 기준
    results = model.predict(frame, conf=0.3, iou=0.45, verbose=False)

    # 6. 결과 시각화
    # results[0].plot()은 바운딩 박스, 클래스명, 신뢰도를 자동으로 그려줍니다.
    annotated_frame = results[0].plot()

    # 화면에 출력
    cv2.imshow("Ship Detection Test", annotated_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
print("--- 테스트가 종료되었습니다. ---")