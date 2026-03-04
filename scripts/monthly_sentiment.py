import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\chara\OneDrive\Desktop\AI-Employee-Sentiment-Project\data\sentiment_output.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Monthly sentiment count
monthly_sentiment = df.groupby(df["Date"].dt.to_period("M"))["Sentiment"].value_counts()

print("Monthly Sentiment Score:")
print(monthly_sentiment)