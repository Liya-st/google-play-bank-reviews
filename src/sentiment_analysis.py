# sentiment_analysis.py

import pandas as pd
from transformers import pipeline

df = pd.read_csv('src/bank_reviews.csv')

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(row):
    try:
        result = sentiment_pipeline(row[:512])[0]
        label = result['label']
        score = result['score']
        return pd.Series([label, score])
    except:
        return pd.Series(["ERROR", 0.0])

df[['sentiment_label', 'sentiment_score']] = df['review'].apply(get_sentiment)

df.to_csv("outputs/sentiment_labeled.csv", index=False)
