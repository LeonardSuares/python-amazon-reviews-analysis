import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import re
from utils import load_data


# 1. Helper Function (Define this first)
def clean_review_text(text):
    if not isinstance(text, str):
        return ""
    # Swap <br> tags for actual newlines
    text = re.sub(r'<br\s*/?>', '\n', text)
    # Strip out any remaining <b>, <i>, etc.
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()


st.title("Reviewer Behavior Analysis")

# 2. Data Preparation
df = load_data()

# Logic: Identify frequent reviewers
user_counts = df['UserId'].value_counts()
df['viewer_type'] = df['UserId'].apply(lambda x: "Frequent" if user_counts[x] > 50 else "Not Frequent")

# Calculate length based on clean text
df['Text_length'] = df['Text'].apply(lambda x: len(str(x).split(' ')))

st.subheader("Review Length: Frequent vs. Non-Frequent")

# --- IMPROVED VISUALIZATION ---
# Set theme for a "lighter" feel
sns.set_theme(style="white", palette="pastel")
plt.rcParams['figure.dpi'] = 200  # Sharpness fix

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# Frequent (using a modern blue)
sns.boxplot(y=df[df['viewer_type'] == 'Frequent']['Text_length'],
            ax=ax1, color="#7eb0d5", width=0.5, linewidth=1.5)
ax1.set_title('Frequent Reviewers (>50 reviews)', fontweight='bold')
ax1.set_ylabel('Word Count')
ax1.set_ylim(0, 600)

# Non-Frequent (using a modern coral/salmon)
sns.boxplot(y=df[df['viewer_type'] == 'Not Frequent']['Text_length'],
            ax=ax2, color="#fd7f6f", width=0.5, linewidth=1.5)
ax2.set_title('Non-Frequent Reviewers', fontweight='bold')
ax2.set_ylabel('')

# Remove those "chunky" black borders
sns.despine(left=True)
plt.tight_layout()

st.pyplot(fig)

st.info("Frequent reviewers tend to have a more consistent review length compared to casual users.")

st.divider()

# 3. Sample Reviews Section
st.subheader("📝 Sample Reviews by User Type")
type_choice = st.radio("Select Reviewer Type", ["Frequent", "Not Frequent"])

# Filter and Sample
sample_df = df[df['viewer_type'] == type_choice]
if not sample_df.empty:
    sample_review = sample_df.sample(1).iloc[0]

    # CLEAN THE TEXT BEFORE DISPLAYING
    cleaned_text = clean_review_text(sample_review['Text'])

    st.chat_message("user").write(f"**Score: {sample_review['Score']}/5**")
    st.write(cleaned_text)  # This will now show proper line breaks
else:
    st.warning("No data found for this category.")