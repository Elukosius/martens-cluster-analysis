import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

def extract_summary_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.select_one("div.left-content > h1")
        date = soup.select_one("div.news-info-box > p.post-date")
        author = soup.select_one("div.author-block > p.author-title")

        summary_div = soup.select_one("div.content-wth-msg")
        if summary_div:
            summary_paragraphs = summary_div.find_all("p")
            summary = " ".join(p.get_text(strip=True) for p in summary_paragraphs[:5])
        else:
            summary = ""

        pdf_link_tag = soup.select_one('div.wp-block-button.aligncenter > a.button[href$=".pdf"]')
        pdf_link = pdf_link_tag["href"] if pdf_link_tag else ""

        return {
            "url": url,
            "title": title.get_text(strip=True) if title else "",
            "date": date.get_text(strip=True) if date else "",
            "author": author.get_text(strip=True) if author else "",
            "summary": summary,
            "pdf_link": pdf_link
        }

    except Exception as e:
        return {
            "url": url,
            "title": "",
            "date": "",
            "author": "",
            "summary": f"ERROR: {e}",
            "pdf_link": ""
        }


df_links = pd.read_csv("links.csv")
results = []

print("🔍 Scraping Martens Centre papers...")
for i, url in enumerate(df_links["link"]):
    result = extract_summary_from_url(url)
    results.append(result)
    print(f"[{i+1}] {result['title'][:60]}...")
    time.sleep(1.0)  # Polite scraping

df_summary = pd.DataFrame(results)
df_summary.to_csv("wmc_summaries.csv", index=False)
print("Finished. Data saved to: wmc_summaries.csv")
