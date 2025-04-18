import os

DATASET_ROOT = "/home/piawsa6000/nas192/tmp/jsi/PETA dataset"
LABEL_FILENAME = "Label.txt"
VALID_EXTS = ["bmp", "jpg", "jpeg", "png"]

MALE_TAG = "personalMale"
FEMALE_TAG = "personalFemale"

summary = []

for folder_name in os.listdir(DATASET_ROOT):
    folder_path = os.path.join(DATASET_ROOT, folder_name)
    archive_path = os.path.join(folder_path, "archive")
    label_path = os.path.join(archive_path, LABEL_FILENAME)

    if not os.path.isdir(archive_path):
        continue

    all_imgs = [
        img for img in os.listdir(archive_path)
        if img.split(".")[-1].lower() in VALID_EXTS
    ]
    total_img_count = len(all_imgs)

    label_count = 0
    male_count = 0
    female_count = 0
    matched_files = 0

    if os.path.isfile(label_path):
        with open(label_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 2:
                    continue
                index = parts[0]
                label_list = parts[1:]
                label_count += 1

                if MALE_TAG in label_list:
                    male_count += 1
                elif FEMALE_TAG in label_list:
                    female_count += 1

                # 이미지가 실제 있는지 확인
                matched = any([
                    img for img in all_imgs
                    if img.startswith(f"{index}_")
                ])
                if matched:
                    matched_files += 1

    summary.append({
        "folder": folder_name,
        "total_images": total_img_count,
        "label_lines": label_count,
        "male": male_count,
        "female": female_count,
        "label_matched_files": matched_files
    })

# 출력
print(f"{'폴더명':<12} {'총이미지':>8} {'라벨수':>8} {'남':>5} {'여':>5} {'매칭됨':>8}")
print("-" * 60)
for row in summary:
    print(f"{row['folder']:<12} {row['total_images']:>8} {row['label_lines']:>8} {row['male']:>5} {row['female']:>5} {row['label_matched_files']:>8}")

# 전체 요약
total_all = sum(r['total_images'] for r in summary)
total_labeled = sum(r['label_lines'] for r in summary)
total_matched = sum(r['label_matched_files'] for r in summary)
total_male = sum(r['male'] for r in summary)
total_female = sum(r['female'] for r in summary)

print("\n📊 전체 요약")
print(f"  총 이미지 수           : {total_all}")
print(f"  라벨 존재하는 줄 수    : {total_labeled}")
print(f"  성별이 명확한 라벨 수  : {total_male + total_female}")
print(f"  실제 이미지 매칭된 수  : {total_matched}")
