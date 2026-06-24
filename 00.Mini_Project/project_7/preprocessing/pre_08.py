import os
import cv2
from ultralytics import YOLO


def run_port_detection():
    # 1. 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 학습 시 생성된 최신 가중치 파일 경로
    weights_path = os.path.join(current_dir, 'ship_project', 'detect_scale_v1', 'weights', 'best.pt')

    if not os.path.exists(weights_path):
        print(f"❌ 가중치 파일을 찾을 수 없습니다: {weights_path}")
        print("학습이 완료된 후 'best.pt' 파일이 해당 경로에 있는지 확인해주세요.")
        return

    # 2. 모델 로드 및 영상 소스 설정
    model = YOLO(weights_path)

    # 분석할 영상 파일명: 항구안큰바다(만).mp4
    video_name = '항구안큰바다(만).mp4'
    video_path = os.path.join(current_dir, video_name)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"❌ 영상을 열 수 없습니다: {video_path}")
        print("파일명에 오타가 없거나, 파일이 코드와 같은 폴더에 있는지 확인하세요.")
        return

    # 3. 결과 영상 저장을 위한 설정
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 결과 파일명: result_port_detection.mp4 (기존 영상 덮어쓰기 방지)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('result_port_detection.mp4', fourcc, fps, (w, h))

    print(f"\n--- [탐지 시작] 분석 영상: {video_name} ---")
    print("화면 종료를 원하시면 'q'를 누르세요.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("영상 재생 및 분석이 완료되었습니다.")
            break

        # 4. YOLO 모델로 예측 (RTX 5060 GPU 가속)
        # conf=0.3: 신뢰도가 30% 이상인 것만 표시 (선박 탐지 시 적절한 기준)
        results = model.predict(frame, conf=0.3, device=0, verbose=False)

        # 5. 결과 시각화
        # 선박의 이름과 신뢰도가 박스와 함께 프레임에 그려짐
        annotated_frame = results[0].plot()

        # 화면 출력 (윈도우 제목 수정)
        cv2.imshow("Marine Surveillance System - Port Analysis", annotated_frame)

        # 파일 저장
        out.write(annotated_frame)

        # 'q' 키를 누르면 루프 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 6. 자원 해제
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("\n--- 분석 완료: 결과가 'result_port_detection.mp4'로 저장되었습니다. ---")


if __name__ == "__main__":
    run_port_detection()