import os
import cv2
import random
import shutil
import glob
import numpy as np
from ultralytics import YOLO
from tqdm import tqdm  # 진행률 표시 라이브4러리

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
train_img_path = os.path.join(current_dir, 'train', 'images')
train_lbl_path = os.path.join(current_dir, 'train', 'labels')
val_img_path = os.path.join(current_dir, 'val', 'images')
val_lbl_path = os.path.join(current_dir, 'val', 'labels')
yaml_path = os.path.join(current_dir, 'data.yaml')


# ==========================================
# 2. HSV 전처리 함수
# ==========================================
def augment_hsv(image_path, save_path):
    img = cv2.imread(image_path)
    if img is None: return
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.add(s, 30)
    v = cv2.add(v, 20)
    final_hsv = cv2.merge((h, s, v))
    enhanced_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite(save_path, enhanced_img)


# ==========================================
# 3. 데이터 증강 실행 (tqdm으로 진행률 표시)
# ==========================================
print("\n--- [1단계] HSV 데이터 증강 시작 ---")
existing_images = [f for f in os.listdir(train_img_path) if f.endswith(('.jpg', '.png')) and 'hsv_' not in f]

# tqdm을 사용하여 반복문 진행률을 %로 표시
for img_name in tqdm(existing_images, desc="전처리 진행 중", unit="img"):
    old_path = os.path.join(train_img_path, img_name)
    new_img_name = 'hsv_' + img_name
    new_path = os.path.join(train_img_path, new_img_name)

    if not os.path.exists(new_path):
        augment_hsv(old_path, new_path)

    old_lbl_name = os.path.splitext(img_name)[0] + '.txt'
    new_lbl_name = 'hsv_' + old_lbl_name
    old_lbl_path = os.path.join(train_lbl_path, old_lbl_name)
    new_lbl_path = os.path.join(train_lbl_path, new_lbl_name)

    if os.path.exists(old_lbl_path) and not os.path.exists(new_lbl_path):
        shutil.copy(old_lbl_path, new_lbl_path)

print(f"--- 증강 완료: 총 {len(existing_images) * 2}개의 학습 데이터 확보 ---")

# ==========================================
# 4. 데이터 분할
# ==========================================
if not os.path.exists(val_img_path):
    os.makedirs(val_img_path, exist_ok=True)
    os.makedirs(val_lbl_path, exist_ok=True)
    images = [f for f in os.listdir(train_img_path) if f.endswith(('.jpg', '.png'))]
    val_images = random.sample(images, int(len(images) * 0.2))
    for name in tqdm(val_images, desc="검증 데이터 분할 중"):
        shutil.move(os.path.join(train_img_path, name), os.path.join(val_img_path, name))
        lbl = os.path.splitext(name)[0] + '.txt'
        if os.path.exists(os.path.join(train_lbl_path, lbl)):
            shutil.move(os.path.join(train_lbl_path, lbl), os.path.join(val_lbl_path, lbl))

# ==========================================
# 5. YOLOv8 재학습 (YOLO 자체 ProgressBar 사용)
# ==========================================
model = YOLO('yolov8n.pt')
print("\n--- [2단계] YOLO 모델 학습 시작 ---")
# YOLOv8은 기본적으로 Epoch마다 진행률을 %와 시간으로 출력합니다.
model.train(
    data=yaml_path,
    epochs=30,
    imgsz=640,
    device='cpu',
    workers=0,
    verbose=True  # 학습 과정을 상세히 출력
)

# ==========================================
# 6. 영상 테스트
# ==========================================
print("\n--- [3단계] 실시간 영상 테스트 시작 ---")
weights_path = os.path.join(current_dir, 'runs', 'detect', 'train*', 'weights', 'best.pt')
best_weights_list = sorted(glob.glob(weights_path))
if not best_weights_list:
    print("학습된 모델을 찾을 수 없습니다.")
else:
    best_weights = best_weights_list[-1]
    trained_model = YOLO(best_weights)
    video_path = os.path.join(current_dir, 'ship_video_01.mp4')
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        success, frame = cap.read()
        if not success: break
        results = trained_model.predict(frame, conf=0.3, verbose=False)
        cv2.imshow("HSV Enhanced Detection", results[0].plot())
        if cv2.waitKey(1) & 0xFF == ord("q"): break

    cap.release()
    cv2.destroyAllWindows()