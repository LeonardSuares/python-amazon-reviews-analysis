import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

st.set_page_config(layout="wide") # Optional: Gives your charts more horizontal room
st.title("Product Review Analysis")

# 1. Load data
df = load_data()

# 2. Logic to filter products
prod_count = df['ProductId'].value_counts().reset_index()
prod_count.columns = ['ProductId', 'count']
freq_prod_ids = prod_count[prod_count['count'] > 500]['ProductId'].values
freq_prod_df = df[df['ProductId'].isin(freq_prod_ids)]

# --- IMPROVED VISUALIZATION SETTINGS ---
# Set a global clean style
sns.set_theme(style="whitegrid", font="sans-serif")
plt.rcParams['figure.dpi'] = 300 # Sharpness fix

st.subheader("Frequency of Products with Over 500 Reviews")

# 3. Main Chart Logic
fig, ax = plt.subplots(figsize=(12, 14)) # Slightly wider

sns.countplot(
    y='ProductId',
    data=freq_prod_df,
    hue='Score',
    order=freq_prod_df['ProductId'].value_counts().index,
    palette="flare", # Modern, cohesive color scale
    ax=ax,
    linewidth=0.5,
    edgecolor="white"
)

# Style Overhaul
ax.set_title('Product Score Distribution (High Volume)', fontsize=16, pad=20, fontweight='bold')
ax.set_xlabel('Number of Reviews', fontsize=12, color='#666666')
ax.set_ylabel('Product ID', fontsize=12, color='#666666')

# Move legend outside so it's not "chunky" or blocking data
ax.legend(title='Score', bbox_to_anchor=(1.05, 1), loc='upper left', frameon=False)

# Remove the boxy look
sns.despine(left=True, bottom=True)

st.pyplot(fig)

# Stats Section
col1, col2 = st.columns(2)
with col1:
    st.metric("Unique Products", df['ProductId'].nunique())
with col2:
    st.metric("High Volume Products (>500)", len(freq_prod_ids))

st.divider()

# 4. Individual Product Lookup
st.subheader("🔎 Individual Product Lookup")
selected_prod = st.selectbox("Select a Product ID to inspect", freq_prod_ids)

prod_data = df[df['ProductId'] == selected_prod]

# Make this chart smaller and cleaner too
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.countplot(
    x='Score',
    data=prod_data,
    ax=ax2,
    palette="viridis",
    width=0.6
)
ax2.set_title(f"Score Distribution for {selected_prod}", fontweight='bold')
sns.despine() # Clean up borders

st.pyplot(fig2)