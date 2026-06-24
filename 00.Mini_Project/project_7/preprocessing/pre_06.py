import torch
from ultralytics import YOLO
import os


def train_model():
    # 1. GPU 장치 확인
    # RTX 5060을 인식하기 위해 torch.cuda가 True여야 합니다.
    if torch.cuda.is_available():
        device_name = torch.cuda.get_device_name(0)
        print(f"✅ GPU 인식 성공: {device_name}")
    else:
        print("❌ GPU를 인식할 수 없습니다. CPU로 학습하면 매우 느립니다.")
        print("지인이 알려준 'pip install ... cu128' 명령어를 다시 확인하세요.")
        return

    # 2. 모델 로드
    # 처음 시작하신다면 가장 가볍고 빠른 'yolov8n.pt' 또는 'yolo11n.pt'를 추천합니다.
    model = YOLO('yolov8n.pt')

    # 3. 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(current_dir, 'data.yaml')

    print(f"\n--- [학습 시작] RTX 5060 가속 모드로 학습을 진행합니다 ---")

    # 4. 모델 학습 실행
    model.train(
        data=yaml_path,  # 데이터셋 설정 파일 (train/val 경로가 적힌 파일)
        epochs=50,  # 학습 횟수 (데이터가 많아졌으니 50회 정도 권장)
        imgsz=640,  # 이미지 크기 (전처리한 이미지 크기와 맞춤)
        batch=16,  # RTX 5060 메모리에 적합한 크기 (속도가 빠르면 32로 올리셔도 됩니다)
        device=0,  # ⭐ 반드시 0 (GPU)으로 설정
        workers=8,  # CPU가 데이터를 GPU로 넘겨주는 속도 (본인 CPU 코어 수에 맞춰 조절)
        amp=True,  # ⭐ RTX 시리즈의 핵심 기능: 자동 혼합 정밀도로 속도 대폭 향상
        mosaic=1.0,  # YOLO의 강력한 증강 기법 (작은 선박 인식률 향상)
        project='ship_project',  # 결과가 저장될 폴더 이름
        name='detect_scale_v1',  # 이번 학습의 세부 이름
        exist_ok=True  # 동일 폴더명 있어도 덮어쓰기/유지
    )

    print("\n--- 학습 완료! ---")
    print(f"최종 모델은 'runs/detect/ship_project/detect_scale_v1/weights/best.pt'에 저장됩니다.")


if __name__ == "__main__":
    train_model()