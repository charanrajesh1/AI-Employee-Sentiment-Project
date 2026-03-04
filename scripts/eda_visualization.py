import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load sentiment dataset
df = pd.read_csv(r"C:\Users\chara\OneDrive\Desktop\AI-Employee-Sentiment-Project\data\sentiment_output.csv")

# Plot sentiment distribution
sns.countplot(x="Sentiment", data=df)

plt.title("Sentiment Distribution of Employee Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()