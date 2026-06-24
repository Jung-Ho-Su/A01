import os
import json
import shutil
import xml.etree.ElementTree as ET
from tqdm import tqdm

CLASSES = ['ship']
ROOT = './voc'
OUTPUT_ROOT = './coco'

def get_coco_template():
    return {
        "info": {
            "description": "Maritime Detection Dataset",
            "url": "https://www.x-mol.com/groups/MIPC",
            "version": "1.0",
            "year": 2026,
            "contributor": "MIPC",
            "date_created": "2026/01/01"
        },
        "licenses": [
            {
                "url": "https://www.x-mol.com/groups/MIPC",
                "id": 1,
                "name": "Attribution License"
            }
        ],
        "images": [],
        "annotations": [],
        "categories": []
    }


def process_subset(root_dir, list_filename, subset_name, classes):
    coco_format = get_coco_template()
    for i, cls in enumerate(classes):
        coco_format["categories"].append({"id": i + 1, "name": cls, "supercategory": "none"})

    txt_path = os.path.join(root_dir, 'ImageSets', 'Main', list_filename)
    xml_dir = os.path.join(root_dir, 'Annotations')
    src_img_dir = os.path.join(root_dir, 'JPEGImages')

    target_img_folder = os.path.join(OUTPUT_ROOT, subset_name)
    json_folder = os.path.join(OUTPUT_ROOT, 'annotations')
    output_json = os.path.join(json_folder, f"{subset_name}.json")

    if not os.path.exists(txt_path):
        print(f"Skipping: {txt_path} not found.")
        return

    os.makedirs(target_img_folder, exist_ok=True)
    os.makedirs(json_folder, exist_ok=True)

    with open(txt_path, 'r') as f:
        file_names = [line.strip() for line in f.readlines() if line.strip()]

    ann_id = 1
    image_id = 1

    print(f"\nProcessing subset: {subset_name}")
    for name in tqdm(file_names, desc="Progress", unit="img"):
        img_file = name + '.jpg'
        src_img = os.path.join(src_img_dir, img_file)

        if os.path.exists(src_img):
            shutil.copy(src_img, os.path.join(target_img_folder, img_file))
        else:
            print(f" Warning: Image {src_img} not found.")
            continue

        xml_file = os.path.join(xml_dir, name + '.xml')
        if not os.path.exists(xml_file):
            continue

        tree = ET.parse(xml_file)
        root = tree.getroot()
        size = root.find('size')

        coco_format["images"].append({
            "id": image_id,
            "file_name": img_file,
            "width": int(size.find('width').text),
            "height": int(size.find('height').text),
            "license": 1,
            "date_captured": "2025-07-01",
            "flickr_url": "https://www.x-mol.com/groups/MIPC",
            "coco_url": "https://www.x-mol.com/groups/MIPC"
        })

        for obj in root.findall('object'):
            cls_name = obj.find('name').text
            if cls_name not in classes:
                continue

            bndbox = obj.find('bndbox')
            xmin, ymin = float(bndbox.find('xmin').text), float(bndbox.find('ymin').text)
            xmax, ymax = float(bndbox.find('xmax').text), float(bndbox.find('ymax').text)
            w, h = xmax - xmin, ymax - ymin

            coco_format["annotations"].append({
                "id": ann_id,
                "image_id": image_id,
                "category_id": classes.index(cls_name) + 1,
                "bbox": [xmin, ymin, w, h],
                "area": w * h,
                "segmentation": [],
                "iscrowd": 0
            })
            ann_id += 1
        image_id += 1

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(coco_format, f, indent=4)
    print(f"Success: Generated {output_json}")


if __name__ == "__main__":

    tasks = [
        ('train.txt', 'train'),
        ('val.txt', 'val'),
    ]

    for txt, subset_name in tasks:
        process_subset(ROOT, txt, subset_name, CLASSES)

    print(f"\nDone!")
