# Policy Paper Theme & Cluster Analysis (Martens Centre)

This project conducts a comprehensive text analysis of policy papers published by the Wilfried Martens Centre for European Studies. Using a combination of Natural Language Processing (NLP), semantic embeddings, clustering, and keyword extraction, the notebook identifies thematic structures and content patterns across a body of policy research.

---

## Objectives

- **Clean** and preprocess raw full-text PDF documents.
- **Detect dominant themes** in each paper using sentence embeddings.
- **Cluster** themes into higher-level topic areas.
- **Visualize** theme co-occurrence, distribution by cluster, and representative keywords.
- **Export** structured CSV summaries for further reporting or visual use.

---

## Scripts Overview

The following Python scripts are provided in the `scripts/` directory to replicate the data acquisition process:

- `download_martens_pdfs.py`: Downloads policy paper PDFs from Martens Centre.
- `download_multi_pdfs.py`: Alternate downloader for a list of PDF links.
- `extract.texts.py`: Extracts full text from PDFs and saves it to `martens_texts.csv`.
- `scrape_summaries.py`: Scrapes metadata and summaries from article pages using BeautifulSoup. These outputs were used for manual reference and exploratory analysis but are not integrated into the final pipeline.

These scripts allow you to regenerate the dataset if the structure of `martens_texts.csv` is lost or if new papers are added in the future.

---

## Input Data

- `martens_texts.csv` — Full-text of Martens Centre policy papers (preprocessed)

---

## Tools & Methods

| Methodology                    | Description |
|-------------------------------|-------------|
| `SentenceTransformers`        | Semantic embeddings for papers and themes |
| `cosine_similarity`           | Theme-matching and clustering |
| `AgglomerativeClustering`     | Grouping themes into macro-clusters |
| `matplotlib`, `seaborn`       | Visualizations (heatmaps, bar charts) |
| `wordcloud`                   | Word cloud of dominant filtered terms |

---

## Outputs

| Output                        | File                      | Description |
|------------------------------|---------------------------|-------------|
| Top 20 Words/Article         | `top_20_words_per_article.csv` | Frequent terms post-cleaning |
| Descriptive Stats            | `text_descriptives_summary.csv` | Basic metrics pre/post-cleaning |
| Theme Counts                 | `theme_counts_table.csv`  | Frequency of assigned themes |
| Cluster Counts               | `cluster.csv`             | Papers per cluster label |
| Top Papers/Cluster           | `top_representative_papers.csv` | Most representative papers |
| Theme Summary Table          | `theme_summary_table.csv` | Theme-cluster-keyword breakdown |
| Visuals                      | PNGs exported (wordcloud, heatmaps, dendrogram) |

---

## Theming

Themes were grouped into 5 higher-level clusters:

1. **Society, Politics & Information Order**
2. **Geopolitics & Strategic Regions**
3. **Economy, Energy & Innovation**
4. **Social Europe & Labour Dynamics**
5. **Defence & Transatlantic Security**

Each theme was mapped to keywords and matched via semantic similarity to papers.

---

## How to Use

1. Clone this repository
2. Open `Analysis.ipynb` in JupyterLab or VSCode
3. Run cells top to bottom — intermediate `.csv` and `.png` files are saved automatically

---

## Author

**Edvardas Lukošius**  
Vilnius, Lithuania  

