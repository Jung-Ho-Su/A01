import cv2
import os
from ultralytics import YOLO


def test_on_video():
    # 1. 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 학습 시 설정한 project와 name 경로에 맞춰 best.pt 경로를 지정합니다.
    # 만약 경로가 다르다면 직접 수정이 필요합니다.
    weights_path = os.path.join(current_dir, 'ship_project', 'detect_scale_v1', 'weights', 'best.pt')
    video_path = os.path.join(current_dir, 'koko.mp4')

    # 2. 모델 로드 (RTX 5060 사용을 위해 device='cuda' 권장)
    if not os.path.exists(weights_path):
        print(f"❌ 가중치 파일을 찾을 수 없습니다: {weights_path}")
        return

    model = YOLO(weights_path)

    # 3. 비디오 파일 열기
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"❌ 영상을 열 수 없습니다: {video_path}")
        return

    print(f"✅ 테스트 시작: {video_path}")
    print("창을 닫으려면 'q' 키를 누르세요.")

    # 4. 실시간 탐지 루프
    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            print("영상 재생이 완료되었습니다.")
            break

        # 모델 예측 (RTX 5060 가속 활용)
        # conf=0.25: 신뢰도 25% 이상만 출력
        # iou=0.45: 박스 중복 제거 강도
        results = model.predict(frame, conf=0.25, iou=0.45, device=0, verbose=False)

        # 결과 시각화 (인식된 객체명과 신뢰도가 박스와 함께 그려짐)
        annotated_frame = results[0].plot()

        # 5. 화면 출력
        cv2.imshow("Ship Project - KOKO.MP4 Test", annotated_frame)

        # 'q' 키 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()
    print("--- 테스트 종료 ---")


if __name__ == "__main__":
    test_on_video()