import pandas as pd

df = pd.read_csv(r"C:\Users\chara\OneDrive\Desktop\AI-Employee-Sentiment-Project\data\sentiment_output.csv")

# Positive feedback ranking
positive = df[df["Sentiment"] == "Positive"]

ranking = positive.groupby("EmployeeID").size().sort_values(ascending=False)

print("Employee Ranking (based on positive sentiment):")
print(ranking)