import os
import random
import shutil
import glob
import cv2
from ultralytics import YOLO

# 1. 경로 설정 (현재 파일이 실행되는 위치 기준)
# C:\Project\Project_source\AI01\Mini_Project\project_7\preprocessing 폴더를 기준으로 설정됩니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
train_img_path = os.path.join(current_dir, 'train', 'images')
train_lbl_path = os.path.join(current_dir, 'train', 'labels')
val_img_path = os.path.join(current_dir, 'val', 'images')
val_lbl_path = os.path.join(current_dir, 'val', 'labels')
yaml_path = os.path.join(current_dir, 'data.yaml')

# 2. 데이터셋 분할 (Val 폴더가 없을 경우에만 1회 실행)
if not os.path.exists(val_img_path):
    os.makedirs(val_img_path, exist_ok=True)
    os.makedirs(val_lbl_path, exist_ok=True)

    if os.path.exists(train_img_path):
        images = [f for f in os.listdir(train_img_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
        val_count = int(len(images) * 0.2)
        val_images = random.sample(images, val_count)

        print(f"--- 데이터 분할: {val_count}개를 val 폴더로 이동 ---")
        for img_name in val_images:
            shutil.move(os.path.join(train_img_path, img_name), os.path.join(val_img_path, img_name))
            lbl_name = os.path.splitext(img_name)[0] + '.txt'
            if os.path.exists(os.path.join(train_lbl_path, lbl_name)):
                shutil.move(os.path.join(train_lbl_path, lbl_name), os.path.join(val_lbl_path, lbl_name))

# 3. data.yaml 경로 자동 수정
if os.path.exists(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(yaml_path, 'w', encoding='utf-8') as f:
        for line in lines:
            if line.startswith('train:'):
                f.write(f"train: {train_img_path}\n")
            elif line.startswith('val:') or line.startswith('valid:'):
                f.write(f"val: {val_img_path}\n")
            else:
                f.write(line)
    print("--- data.yaml 경로 최신화 완료 ---")

# 4. YOLOv8 학습
model = YOLO('yolov8n.pt')
print("--- 학습 시작 ---")
model.train(
    data=yaml_path,
    epochs=10,
    imgsz=640,
    device='cpu',
    workers=0  # 윈도우 환경에서 멀티프로세싱 에러 방지를 위해 0 설정
)

# 5. 영상 검증 (가장 최신 학습 결과 자동 탐색)
print("--- 영상 검증 시작 ---")
# 'runs/detect/train*/weights/best.pt' 패턴으로 모든 결과물 탐색
search_pattern = os.path.join(current_dir, 'runs', 'detect', 'train*', 'weights', 'best.pt')
weights_list = glob.glob(search_pattern)

if weights_list:
    # 가장 최근에 생성된 폴더의 모델 선택
    best_model_path = sorted(weights_list)[-1]
    print(f"✅ 사용 모델 경로: {best_model_path}")

    trained_model = YOLO(best_model_path)
    video_path = os.path.join(current_dir, 'ship_video_01.mp4')

    if os.path.exists(video_path):
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            success, frame = cap.read()
            if not success: break

            results = trained_model.predict(frame, conf=0.3)
            annotated_frame = results[0].plot()

            cv2.imshow("Ship Detection Result", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"): break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print(f"❌ 영상 파일을 찾을 수 없습니다: {video_path}")
else:
    print("❌ 학습 결과물(best.pt)이 생성되지 않았습니다. 학습 로그를 확인하세요.")
