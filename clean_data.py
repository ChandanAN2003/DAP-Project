import pandas as pd
import re
from textblob import TextBlob

# Load uncleaned data
df = pd.read_csv("uncleaned_travel_data.csv")

# Drop rows with missing essentials
df.dropna(subset=['location', 'mood', 'memory'], inplace=True)
df['location'] = df['location'].str.strip().str.title()
df['mood'] = df['mood'].str.strip().str.capitalize()

def clean_memory(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    return text.strip().capitalize()

df['memory'] = df['memory'].astype(str).apply(clean_memory)

# Sentiment analysis
df['sentiment'] = df['memory'].apply(lambda t: (
    'Positive' if TextBlob(t).sentiment.polarity > 0 else
    'Negative' if TextBlob(t).sentiment.polarity < 0 else 'Neutral'))

# Save cleaned data
df.to_csv("cleaned_travel_data.csv", index=False)
print("✅ Cleaned data saved to cleaned_travel_data.csv")
