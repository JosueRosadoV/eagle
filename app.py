import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

# Load your dataset
df = pd.read_csv("expanded_eagle_island_sentiment_dataset.csv")
df['Date'] = pd.to_datetime(df['Date'])

st.title("Eagle Island Camp: Camper Sentiment Dashboard")
st.markdown("Explore camper feedback trends, sentiment breakdowns, and key insights.")

# Sidebar Filters
with st.sidebar:
    st.header("Filter")
    program_filter = st.selectbox("Choose a program:", ["All"] + sorted(df['Program Name'].unique().tolist()))

# Apply filter
if program_filter != "All":
    df = df[df["Program Name"] == program_filter]

# Sentiment trend line
st.subheader("📈 Sentiment Over Time")
sentiment_trend = df.groupby([df['Date'].dt.to_period('M'), 'Sentiment Label']).size().unstack().fillna(0)
fig, ax = plt.subplots()
sentiment_trend.plot(ax=ax)
st.pyplot(fig)

# Word clouds
st.subheader("🌀 Word Clouds by Sentiment")

for sentiment in ["Positive", "Negative", "Neutral"]:
    st.markdown(f"**{sentiment} Feedback**")
    text = " ".join(df[df["Sentiment Label"] == sentiment]["Feedback Text"])
    if text:
        wordcloud = WordCloud(width=800, height=300, background_color="white").generate(text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.write("No data available.")

# Insights
st.subheader("🧠 Key Insights & Recommendations")
st.markdown("""
- **Campfire nights** and **supportive counselors** are frequently mentioned in positive reviews.
- **Bugs**, **cold nights**, and **lack of indoor alternatives** appear in negative reviews.
- Increase **social bonding events**, provide **more weather-related comfort**, and **shorten demanding activities** like full-day sailing.
""")
print('Hello World')