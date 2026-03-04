import pandas as pd

df = pd.read_csv(r"C:\Users\chara\OneDrive\Desktop\AI-Employee-Sentiment-Project\data\sentiment_output.csv")

# Employees with negative sentiment
risk = df[df["Sentiment"] == "Negative"]

flight_risk = risk.groupby("EmployeeID").size()

print("Employees with potential flight risk:")
print(flight_risk)