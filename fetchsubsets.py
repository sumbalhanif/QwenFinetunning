import json
import random
import os

input_file = r"C:\Users\ppmc\Desktop\data\pubtabnet\pubtabnet\PubTabNet_2.0.0.jsonl"
output_folder = r"C:\Users\ppmc\Desktop\MyWork"

print("Opening file:", input_file)

train_entries = []

# Read and filter only training split
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        entry = json.loads(line)
        if entry["split"] == "train":
            train_entries.append(line)

print("Total training samples:", len(train_entries))

# Shuffle
random.shuffle(train_entries)

# Create subsets
subset_2k = train_entries[:2000]
subset_5k = train_entries[:5000]
subset_10k = train_entries[:10000]

# Save subsets
with open(os.path.join(output_folder, "train_2k.jsonl"), "w", encoding="utf-8") as f:
    f.writelines(subset_2k)

with open(os.path.join(output_folder, "train_5k.jsonl"), "w", encoding="utf-8") as f:
    f.writelines(subset_5k)

with open(os.path.join(output_folder, "train_10k.jsonl"), "w", encoding="utf-8") as f:
    f.writelines(subset_10k)

print("Subsets created successfully inside Desktop\\MyWork folder.")

