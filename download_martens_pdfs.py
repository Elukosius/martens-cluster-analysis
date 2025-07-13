import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

# === Config ===
csv_path = "links.csv"
output_dir = "downloaded_pdfs"
os.makedirs(output_dir, exist_ok=True)

# === Load URLs ===
df = pd.read_csv(csv_path)
urls = df.iloc[:, 0].dropna().unique()

def download_pdf_from_page(page_url):
    try:
        res = requests.get(page_url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # Find first .pdf link
        pdf_tag = soup.find("a", href=lambda href: href and href.endswith(".pdf"))
        if not pdf_tag:
            print(f"No PDF found at {page_url}")
            return

        pdf_url = pdf_tag["href"]
        if not pdf_url.startswith("http"):
            pdf_url = f"https://www.martenscentre.eu{pdf_url}"

        # Extract file name from URL
        pdf_filename = os.path.basename(pdf_url)

        # Use URL slug as identifier
        slug = page_url.strip("/").split("/")[-1]
        filename = f"{slug}__{pdf_filename}"
        filepath = os.path.join(output_dir, filename)

        if os.path.exists(filepath):
            print(f"Already exists: {filename}")
            return

        pdf_res = requests.get(pdf_url, timeout=15)
        pdf_res.raise_for_status()

        with open(filepath, "wb") as f:
            f.write(pdf_res.content)
        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Failed for {page_url}: {e}")

# === Loop through all ===
for url in urls:
    print(f"{url}")
    download_pdf_from_page(url)
    time.sleep(1)
