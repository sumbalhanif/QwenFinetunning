import os
import json
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from PIL import Image

# ==============================
# PATHS
# ==============================

base_path = r"C:\Users\ppmc\Desktop\data\FinTabNet\fintabnet"

json_path = os.path.join(base_path, "FinTabNet_1.0.0_table_test.jsonl")
pdf_root = os.path.join(base_path, "pdf")
output_dir = os.path.join(base_path, "fintab_1000")

os.makedirs(output_dir, exist_ok=True)

# ==============================

MAX_TABLES = 1000
count = 0

print("Starting extraction...")

with open(json_path, "r") as f:

    for idx, line in enumerate(f):

        if count >= MAX_TABLES:
            break

        data = json.loads(line)

        pdf_file = data["filename"]   # e.g. HAL/2009/page_77.pdf
        pdf_path = os.path.join(pdf_root, pdf_file)

        if not os.path.exists(pdf_path):
            continue

        try:
            # ---------------- PDF INFO ----------------
            reader = PdfReader(open(pdf_path, "rb"))
            page = reader.pages[0]

            pdf_height = float(page.mediabox.height)
            pdf_width = float(page.mediabox.width)

            # ---------------- IMAGE ----------------
            images = convert_from_path(
                pdf_path,
                size=(int(pdf_width), int(pdf_height))
            )

            img = images[0]

            # ---------------- BBOX ----------------
            x1, y1, x2, y2 = data["bbox"]

            y1_new = pdf_height - y2
            y2_new = pdf_height - y1

            table = img.crop((x1, y1_new, x2, y2_new)).convert("RGB")

            # ---------------- SAFE NAME ----------------
            safe_name = pdf_file.replace("/", "_").replace(".pdf", "")

            save_name = f"{safe_name}_table.png"

            save_path = os.path.join(output_dir, save_name)

            table.save(save_path)

            count += 1

            if count % 100 == 0:
                print(f"{count} tables extracted")

        except Exception as e:
            print("Skipped:", pdf_file)
            continue

print("Finished!")
print("Total extracted:", count)