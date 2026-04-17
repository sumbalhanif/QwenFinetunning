import json
import os

base_path = r"C:\Users\ppmc\Desktop\MyResearchWork"

input_file = os.path.join(base_path, "train_15k.jsonl")
output_file = os.path.join(base_path, "train_15k_chat.jsonl")

instruction_text = """
Extract the complete HTML table structure.

Rules:
- maintain correct row and column alignment
- respect rowspan and colspan
- output valid HTML table only
"""

print("Processing 15K dataset...")

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:
        entry = json.loads(line)

        image_name = entry["filename"]
        structure_tokens = entry["html"]["structure"]["tokens"]
        structure_string = "".join(structure_tokens)

        new_entry = {
            "messages": [
                {
                    "role": "user",
                    "content": "<image>\n" + instruction_text
                },
                {
                    "role": "assistant",
                    "content": structure_string
                }
            ],
            "image": image_name
        }

        outfile.write(json.dumps(new_entry) + "\n")

print("15K dataset converted to chat format successfully.")