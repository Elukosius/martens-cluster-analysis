import os
import time
import requests
from bs4 import BeautifulSoup

pages = [
    "https://www.martenscentre.eu/publication/navigating-through-renewed-economic-uncertainty/",
    "https://www.martenscentre.eu/publication/sustainable-europe-cross-cutting-strategies-for-a-future-proof-union/",
    "https://www.martenscentre.eu/publication/navigating-demographic-dynamics-strategies-for-tomorrow/",
    "https://www.martenscentre.eu/publication/the-future-of-transatlantic-relations/",
    "https://www.martenscentre.eu/publication/overcoming-the-geography-of-discontent-new-perspectives-and-innovative-solutions/"
]

output_dir = "downloaded_pdfs"
os.makedirs(output_dir, exist_ok=True)

def download_pdf(pdf_url, page_slug):
    filename = pdf_url.split("/")[-1]
    unique_filename = f"{page_slug}_{filename}"
    filepath = os.path.join(output_dir, unique_filename)

    if os.path.exists(filepath):
        print(f"Already downloaded: {unique_filename}")
        return

    try:
        response = requests.get(pdf_url, timeout=10)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"⬇Downloaded: {unique_filename}")
    except Exception as e:
        print(f"Failed to download {pdf_url}: {e}")

# === Process all pages ===
for page_url in pages:
    print(f"Checking: {page_url}")
    try:
        res = requests.get(page_url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # Find all <a> tags with href ending in .pdf
        pdf_links = soup.find_all("a", href=lambda href: href and href.endswith(".pdf"))
        slug = page_url.strip("/").split("/")[-1]

        for a in pdf_links:
            pdf_url = a["href"]
            if not pdf_url.startswith("http"):
                pdf_url = f"https://www.martenscentre.eu{pdf_url}"
            download_pdf(pdf_url, slug)
            time.sleep(1)

    except Exception as e:
        print(f"Failed to process page: {e}")
