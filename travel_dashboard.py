import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

st.set_page_config(page_title="Travel Memory Dashboard", layout="wide")
st.title("🧳 Travel Memory Analysis")

df = pd.read_csv("cleaned_travel_data.csv")
st.subheader("📄 Sample Data")
st.dataframe(df.head(10))

# Mood Distribution
st.subheader("🎭 Mood Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x='mood', order=df['mood'].value_counts().index, palette='Set2', ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Top Locations
st.subheader("📍 Top Locations")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, y='location', order=df['location'].value_counts().head(10).index, palette='Set1', ax=ax2)
st.pyplot(fig2)

# Sentiment
st.subheader("💬 Sentiment")
fig3, ax3 = plt.subplots()
sns.countplot(data=df, x='sentiment', palette='coolwarm', ax=ax3)
st.pyplot(fig3)

# Common Words
st.subheader("📝 Frequent Words in Memories")
words = ' '.join(df['memory']).lower().split()
word_freq = dict(Counter(words).most_common(10))
fig4, ax4 = plt.subplots()
sns.barplot(x=list(word_freq.values()), y=list(word_freq.keys()), palette='magma', ax=ax4)
st.pyplot(fig4)

st.markdown("---")
st.markdown("📊 Built with Streamlit | Project by Chandan")
