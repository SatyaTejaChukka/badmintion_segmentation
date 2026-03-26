import cv2
import json
import numpy as np
import os

os.makedirs("data/images", exist_ok=True)
os.makedirs("data/masks", exist_ok=True)

pairs = [
    ("IMG_2426[1].MOV", "IMG_2426[1]_court_annotations.json"),
    ("IMG_2429[1].MOV", "IMG_2429[1]_court_annotations.json"),
    ("mov_1.MOV", "mov_1_court_annotations.json"),
    ("12ft_IMG_2403_6mins.MOV", "12ft_IMG_2403_6mins_court_annotations.json"),

]

count = 0

for video_path, annotation_path in pairs:
    cap = cv2.VideoCapture(video_path)

    with open(annotation_path) as f:
        data = json.load(f)

    annotations = data["annotations"]

    for frame_idx, points in annotations.items():
        frame_idx = int(frame_idx)

        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            continue

        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        pts = np.array(points, dtype=np.int32)

        cv2.fillPoly(mask, [pts], 255)

        cv2.imwrite(f"data/images/{count}.png", frame)
        cv2.imwrite(f"data/masks/{count}.png", mask)

        count += 1

    cap.release()

print("Dataset created with", count, "samples")