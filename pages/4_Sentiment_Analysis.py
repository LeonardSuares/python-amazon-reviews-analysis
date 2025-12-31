import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns  # <-- You need this for boxenplot
from textblob import TextBlob
from collections import Counter
from utils import load_data

st.title("Sentiment Analysis")
df = load_data()

sample_size = st.slider("Select sample size for analysis", 5000, 50000, 20000)

if st.button("Run Analysis"):
    with st.spinner("Calculating polarity..."):
        # 1. Prepare Sample
        sample = df.head(sample_size).copy()

        # 2. Calculation (MUST happen before plotting)
        sample['polarity'] = sample['Summary'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

        # 3. Correlation Chart (Boxenplot)
        st.subheader("Sentiment Polarity vs. Star Rating")
        fig_corr, ax_corr = plt.subplots(figsize=(10, 6))
        sns.boxenplot(x='Score', y='polarity', data=sample, ax=ax_corr, palette="coolwarm")
        ax_corr.set_title("Does Sentiment Match the Star Rating?")
        st.pyplot(fig_corr)
        st.write("_Interpretation: 5-star reviews should have high positive polarity (closer to 1.0)._")

        # 4. Phrase Counters
        pos_reviews = sample[sample['polarity'] > 0]
        neg_reviews = sample[sample['polarity'] < 0]

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Top Positive Phrases")
            pos_counts = Counter(pos_reviews['Summary']).most_common(10)
            st.table(pos_counts)
        with col2:
            st.subheader("Top Negative Phrases")
            neg_counts = Counter(neg_reviews['Summary']).most_common(10)
            st.table(neg_counts)

        # 5. Polarity Distribution
        st.subheader("Overall Sentiment Vibe")
        fig_dist, ax_dist = plt.subplots()
        sample['polarity'].hist(bins=30, ax=ax_dist, color='skyblue', edgecolor='black')
        ax_dist.set_title("Distribution of Sentiment Polarity")
        st.pyplot(fig_dist)

