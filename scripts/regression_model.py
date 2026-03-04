import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\chara\OneDrive\Desktop\AI-Employee-Sentiment-Project\data\sentiment_output.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

# Convert sentiment to numeric
sentiment_score = df["Sentiment"].map({
    "Positive": 1,
    "Neutral": 0,
    "Negative": -1
})

X = df[["Month"]]
y = sentiment_score

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[12]])

print("Predicted sentiment score for month 12:", prediction)