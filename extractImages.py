import json
import os
import shutil

# ===== PATHS =====
base_path = r"C:\Users\ppmc\Desktop\MyWork"
source_image_folder = r"C:\Users\ppmc\Desktop\data\pubtabnet\pubtabnet\train"

subsets = {
    "2k": "train_2k_chat.jsonl",
    "5k": "train_5k_chat.jsonl",
    "10k": "train_10k_chat.jsonl"
}

for key, filename in subsets.items():
    print(f"\nProcessing {key} subset...")

    input_file = os.path.join(base_path, filename)
    output_folder = os.path.join(base_path, f"images_{key}")

    os.makedirs(output_folder, exist_ok=True)

    image_names = set()

    # Read image names from JSON
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            image_names.add(entry["image"])

    print(f"Total images to copy: {len(image_names)}")

    copied = 0

    # Copy images
    for img_name in image_names:
        src_path = os.path.join(source_image_folder, img_name)
        dst_path = os.path.join(output_folder, img_name)

        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            copied += 1
        else:
            print(f"Missing: {img_name}")

    print(f"Copied {copied} images for {key} subset.")

print("\nAll subsets image extraction completed.")