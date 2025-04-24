import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

df = pd.read_csv('expanded_eagle_island_sentiment_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

st.title('Eagle Island Camp sentiment analysis project')
st.markdown('Explore different trends and patterns of sentiments in reviews by campers, parents and staff throughout camp season.')

#filter

st.subheader('Sentiment trends over time')

months = ['June', 'July', 'August']
values = {
    'Mixed': (5,3,6),
    'Negative': (3,5,2),
    'Neutral': (4,6,6),
    'Positive': (6,4,10)
}
x = np.arange(len(months))
width = 0.2
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
for sentiment, count in values.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, count, width, label=sentiment)
    ax.bar_label(rects, padding=1)
    multiplier += 1
ax.set_title('Sentiment trends')
ax.set_xticks(x + width, months)
ax.set_ylabel('Count')
ax.legend();
st.pyplot(fig)