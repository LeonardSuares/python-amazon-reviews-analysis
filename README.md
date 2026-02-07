# 🛒 Amazon User Reviews Analysis Dashboard

**Live Application:** [View on Streamlit Cloud](https://amazon-reviews-analysis-fpn7avhj8gxxcfeayq595h.streamlit.app/Sentiment_Analysis)

## 📖 Project Overview
This project is a high-performance, interactive Streamlit dashboard designed for analyzing over 250,000 Amazon fine food reviews. It demonstrates advanced data engineering techniques, such as Parquet conversion for efficiency, a multi-page app architecture, and natural language processing for sentiment analysis.

---

## 🚀 Live Features

* **Product Analysis:** Explore score distributions and trends for the most reviewed products in the dataset.
* **Reviewer Behavior:** A deep dive into the habits and patterns of "Frequent" vs. "Casual" reviewers to understand user engagement.
* **Sentiment Analysis:** Real-time NLP processing using TextBlob to correlate written review summaries with their corresponding star ratings.
* **Interactive Visuals:** High-quality data storytelling built with Seaborn and Matplotlib for clear and actionable insights.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit (Multi-page architecture)
* **Data Engineering:** Pandas, PyArrow, Brotli (optimized Parquet compression)
* **NLP:** TextBlob
* **Visualization:** Seaborn, Matplotlib

---

## 📂 Project Structure
```text
python-amazon-reviews-analysis/
├── pages/                    # Multi-page application structure
│   ├── Sentiment_Analysis.py
│   └── ...
├── data/                     # Data directory (Parquet files)
├── main.py                   # Entry point for the Streamlit dashboard
├── requirements.txt          # Project dependencies
└── README.md
```

