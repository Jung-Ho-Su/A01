import xml.etree.ElementTree as ET
import shutil
from pathlib import Path
from tqdm import tqdm


classes_names = ["ship"]
data_set = ("train", "val")


def convert_box(size, box):
    dw, dh = 1.0 / size[0], 1.0 / size[1]
    x, y, w, h = (box[0] + box[1]) / 2.0 - 1, (box[2] + box[3]) / 2.0 - 1, box[1] - box[0], box[3] - box[2]
    return x * dw, y * dh, w * dw, h * dh


def convert_label(lb_path, image_id, invalid_file):

    in_file = open(Path(f"./voc/Annotations/{image_id}.xml"))
    out_file = open(lb_path, "w")
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    names = classes_names
    valid = False

    for obj in root.iter("object"):
        cls = obj.find("name").text
        difficult = obj.find("difficult")
        if cls in names and (difficult is None or int(difficult.text) != 1):
            xmlbox = obj.find("bndbox")
            bb = convert_box((w, h), [float(xmlbox.find(x).text) for x in ("xmin", "xmax", "ymin", "ymax")])
            cls_id = names.index(cls)  # class id
            out_file.write(" ".join(str(a) for a in (cls_id, *bb)) + "\n")
            valid = True
        else:
            invalid_file.write(f"Parsing label for: {image_id}  Found class: {cls}  --> Skipped: Not in class list\n")

    out_file.close()
    if not valid or lb_path.stat().st_size == 0:
        lb_path.unlink()
        return False
    return True


if __name__ == "__main__":

    imgs_path = Path("./yolo/images")
    lbs_path = Path("./yolo/labels")
    imgs_path.mkdir(exist_ok=True, parents=True)
    lbs_path.mkdir(exist_ok=True, parents=True)

    invalid_path = Path("./yolo/invalid.txt")
    invalid_file = open(invalid_path, "w")

    for image_set in data_set:

        with open(f"./voc/ImageSets/Main/{image_set}.txt") as f:
            image_ids = f.read().strip().split()

        txt_file = open(f"./yolo/{image_set}.txt", "w")

        print(f"\nProcessing subset: {image_set}")
        for id in tqdm(image_ids, desc="Progress", unit="img"):
            img_path = Path(f"./voc/JPEGImages/{id}.jpg")
            shutil.copy(img_path, imgs_path / img_path.name)

            lb_path = lbs_path / img_path.with_suffix(".txt").name
            valid = convert_label(lb_path, id, invalid_file)
            if valid:
                txt_file.write("./" + (Path("./images") / img_path.name).as_posix() + "\n")

        txt_file.close()

    invalid_file.close()

    if invalid_path.stat().st_size == 0:
        invalid_path.unlink()

    print(f"\nDone!")


    

