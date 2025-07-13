import os
import fitz
import pandas as pd


PDF_FOLDER = "downloaded_pdfs"
pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.lower().endswith('.pdf')]


data = []

for filename in pdf_files:
    file_path = os.path.join(PDF_FOLDER, filename)
    try:
        with fitz.open(file_path) as doc:
            full_text = ""
            for page in doc:
                full_text += page.get_text()
            data.append({"filename": filename, "text": full_text})
    except Exception as e:
        print(f"Error reading {filename}: {e}")

df = pd.DataFrame(data)

df.to_csv("martens_texts.csv", index=False)
print("Extraction complete. Saved to martens_texts.csv")
