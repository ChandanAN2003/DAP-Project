import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load cleaned data
df = pd.read_csv("cleaned_travel_data.csv")

# Page config
st.set_page_config(page_title="Travel Memory Dashboard", layout="wide")
st.title("🧳 Travel Memory Tracker Dashboard")

# --- FILTERS ---
st.sidebar.header("🔍 Filter Data")
locations = st.sidebar.multiselect("Select Locations", sorted(df['location'].unique()))
moods = st.sidebar.multiselect("Select Moods", sorted(df['mood'].unique()))

# Apply filters
if locations:
    df = df[df['location'].isin(locations)]
if moods:
    df = df[df['mood'].isin(moods)]

st.markdown(f"### Showing {len(df)} entries after filtering")

# --- PIE CHART for Mood Distribution ---
st.subheader("🎭 Mood Distribution (Pie)")
mood_counts = df['mood'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(mood_counts, labels=mood_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'))
ax1.axis('equal')
st.pyplot(fig1)

# --- PIE CHART for Sentiment Analysis ---
st.subheader("💬 Sentiment Analysis (Pie)")
sentiment_counts = df['sentiment'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('coolwarm'))
ax2.axis('equal')
st.pyplot(fig2)

# --- SCATTER PLOT of Mood by Date ---
st.subheader("📅 Mood over Time")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
fig3, ax3 = plt.subplots(figsize=(10, 4))
sns.scatterplot(data=df, x='date', y='mood', hue='sentiment', palette='Set1', ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)

# --- BAR: Top Locations ---
st.subheader("📍 Top Locations Visited")
top_locations = df['location'].value_counts().head(10)
fig4, ax4 = plt.subplots()
sns.barplot(x=top_locations.values, y=top_locations.index, palette='Accent', ax=ax4)
st.pyplot(fig4)

# --- WORD FREQUENCY ---
st.subheader("📝 Most Frequent Words in Memories")
words = ' '.join(df['memory']).lower().split()
word_freq = dict(Counter(words).most_common(10))
fig5, ax5 = plt.subplots()
sns.barplot(x=list(word_freq.values()), y=list(word_freq.keys()), palette='magma', ax=ax5)
st.pyplot(fig5)

st.markdown("---")
st.markdown("✨ Made with ❤️ using Streamlit")
