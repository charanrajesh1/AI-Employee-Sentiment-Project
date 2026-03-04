import pandas as pd
from textblob import TextBlob

# Load dataset
df = pd.read_csv(
    r"C:\Users\chara\OneDrive\Desktop\AI-Employee-Sentiment-Project\data\employee_reviews.csv",
    engine="python",
    on_bad_lines="skip"
)

# Sentiment function
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)

# Save result
df.to_csv(
    r"C:\Users\chara\OneDrive\Desktop\AI-Employee-Sentiment-Project\data\sentiment_output.csv",
    index=False
)

print("Sentiment labeling completed.")