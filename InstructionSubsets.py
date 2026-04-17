import json
import os

base_path = r"C:\Users\ppmc\Desktop\MyWork"

subsets = [
    "train_2k.jsonl",
    "train_5k.jsonl",
    "train_10k.jsonl"
]

instruction_text = "Extract the full table structure in HTML format."

for subset in subsets:
    input_file = os.path.join(base_path, subset)
    output_file = os.path.join(base_path, subset.replace(".jsonl", "_chat.jsonl"))

    print(f"Processing {subset}...")

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

    print(f"{subset} converted successfully.")

print("All subsets converted to chat format.")
