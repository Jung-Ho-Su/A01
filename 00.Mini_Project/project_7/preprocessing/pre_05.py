# 전처리 사진 크기 변경
# 0.5,0.7, 1.3, 1.5

import os
import cv2
import numpy as np
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor  # CPU 멀티코어 활용

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
train_img_path = os.path.join(current_dir, 'train', 'images')
train_lbl_path = os.path.join(current_dir, 'train', 'labels')

# 배율 설정
SCALES = [0.5, 0.7, 1.3, 1.5]


def process_single_image(img_name):
    """한 장의 이미지를 4가지 배율로 변환하고 라벨을 복사하는 함수"""
    img_path = os.path.join(train_img_path, img_name)
    img = cv2.imread(img_path)
    if img is None: return

    h, w = img.shape[:2]
    base_name = os.path.splitext(img_name)[0]
    ext = os.path.splitext(img_name)[1]

    # 해당 이미지의 라벨 경로 확인
    lbl_name = base_name + '.txt'
    old_lbl_path = os.path.join(train_lbl_path, lbl_name)

    for s in SCALES:
        # 1. 이미지 크기 변환
        new_w, new_h = int(w * s), int(h * s)
        resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

        # 2. 캔버스 생성 (원본 크기 유지 및 패딩)
        # 선박 감지 시 배경 학습을 위해 원본 크기 캔버스 중앙에 배치
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

        # 복사할 영역 계산 (이미지가 크면 자르고, 작으면 중앙 배치)
        off_h, off_w = min(h, new_h), min(w, new_w)
        target_y, target_x = (h - off_h) // 2, (w - off_w) // 2
        src_y, src_x = (new_h - off_h) // 2, (new_w - off_w) // 2

        canvas[target_y:target_y + off_h, target_x:target_x + off_w] = \
            resized[src_y:src_y + off_h, src_x:src_x + off_w]

        # 3. 저장명 설정 (예: scale_0.5_image.jpg)
        new_img_name = f"scale_{s}_{img_name}"
        cv2.imwrite(os.path.join(train_img_path, new_img_name), canvas)

        # 4. 라벨 복사 (중앙 정렬 방식이므로 기존 라벨 그대로 사용 가능)
        if os.path.exists(old_lbl_path):
            new_lbl_name = f"scale_{s}_{lbl_name}"
            import shutil
            shutil.copy(old_lbl_path, os.path.join(train_lbl_path, new_lbl_name))


def main():
    print("--- 멀티코어 기반 데이터 전처리 시작 ---")
    image_files = [f for f in os.listdir(train_img_path)
                   if f.lower().endswith(('.jpg', '.png', '.jpeg'))
                   and 'scale_' not in f]  # 이미 변환된 파일 중복 방지

    # CPU의 모든 코어를 사용하여 병렬 처리
    # max_workers를 지정하지 않으면 자동으로 최대 코어 수를 사용합니다.
    with ProcessPoolExecutor() as executor:
        list(tqdm(executor.map(process_single_image, image_files),
                  total=len(image_files), desc="전처리 진행률"))

    print(f"--- 전처리 완료: 총 {len(image_files) * len(SCALES)}개의 증강 데이터 생성 ---")


if __name__ == "__main__":
    main()