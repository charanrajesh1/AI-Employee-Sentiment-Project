# **AI Employee Sentiment Analysis Project**

## **Project Overview**

This project analyzes employee feedback data to understand organizational sentiment patterns and identify employee flight risk. By leveraging natural language processing and machine learning, the system provides actionable insights into employee satisfaction, engagement trends, and retention risks.

**Key Value:** Helps organizations proactively identify at-risk employees and address engagement issues before they lead to turnover.

---

## **What This Project Does**

### **1. Sentiment Labeling** (`sentiment_labeling.py`)
- Processes employee reviews and feedback
- Classifies sentiment into three categories: Positive, Negative, Neutral
- Uses natural language processing techniques to analyze text data

### **2. Exploratory Data Analysis (EDA)** (`eda_visualization.py`)
- Generates visualizations of sentiment distribution
- Identifies patterns in employee feedback
- Reveals trends across different segments
- Creates charts like `Figure_1.png` showing key insights

### **3. Monthly Sentiment Scoring** (`monthly_sentiment.py`)
- Aggregates sentiment data over time
- Tracks sentiment trends by month
- Enables time-series analysis of organizational health

### **4. Employee Ranking** (`employee_ranking.py`)
- Ranks employees by sentiment scores
- Identifies high-performing employees (high sentiment)
- Flags at-risk employees (negative sentiment patterns)

### **5. Flight Risk Detection** (`flight_risk.py`)
- Predicts which employees are likely to leave the company
- Uses sentiment patterns as key indicators of flight risk
- Enables HR to take proactive retention measures

### **6. Predictive Modeling** (`regression_model.py`)
- Implements linear regression to model sentiment trends over time
- Forecasts future sentiment patterns
- Helps organizations plan interventions

---

## **Tools & Technologies Used**

**Data Processing:**
- Python 3.x
- Pandas (data manipulation and aggregation)
- NumPy (numerical computations)

**Natural Language Processing & ML:**
- Scikit-learn (sentiment classification, linear regression)
- Text processing for NLP

**Visualization:**
- Matplotlib (trend analysis, distribution plots)

---

## **Project Structure**

```
AI-Employee-Sentiment-Project/
├── data/
│   ├── employee_reviews.csv              # Raw employee review data
│   └── sentiment_output.csv              # Processed sentiment classifications
├── scripts/
│   ├── sentiment_labeling.py             # Sentiment classification module
│   ├── eda_visualization.py              # EDA and visualization generation
│   ├── monthly_sentiment.py              # Monthly trend aggregation
│   ├── employee_ranking.py               # Employee risk ranking system
│   ├── flight_risk.py                    # Flight risk detection logic
│   └── regression_model.py               # Linear regression predictions
├── Figure_1.png                          # Key visualization output
├── README.md                             # Project documentation
└── requirements.txt                      # Python dependencies (if present)
```

---

## **How to Use This Project**

### **1. Review the Scripts**

**Sentiment Labeling:**
- `scripts/sentiment_labeling.py` - Classifies employee reviews as Positive, Negative, or Neutral

**Data Exploration:**
- `scripts/eda_visualization.py` - Generates visualizations (like `Figure_1.png`)
- Explore sentiment distribution and patterns

**Monthly Analysis:**
- `scripts/monthly_sentiment.py` - Aggregates sentiment trends over time
- Tracks organizational health by month

**Risk Assessment:**
- `scripts/employee_ranking.py` - Ranks employees by sentiment score
- `scripts/flight_risk.py` - Identifies at-risk employees

**Predictions:**
- `scripts/regression_model.py` - Linear regression model for sentiment forecasting

### **2. Explore the Data**
- `data/employee_reviews.csv` - Raw employee feedback data
- `data/sentiment_output.csv` - Processed sentiment classifications and scores

### **3. Review Visualizations**
- `Figure_1.png` - Key visualization showing sentiment distribution and insights

### **4. Run the Analysis**
Execute scripts in this order:
```
1. python scripts/sentiment_labeling.py           # Classify sentiments
2. python scripts/eda_visualization.py             # Generate visualizations
3. python scripts/monthly_sentiment.py             # Calculate monthly trends
4. python scripts/employee_ranking.py              # Rank employees
5. python scripts/flight_risk.py                   # Identify flight risk
6. python scripts/regression_model.py              # Build predictive model
```

---

## **Key Findings**

The project delivers several critical insights:

- **Sentiment Distribution:** Breakdown of positive, negative, and neutral feedback in the organization
- **Trend Analysis:** How employee sentiment changes over time (monthly trends)
- **Risk Identification:** Employees with negative sentiment patterns and high flight risk
- **Predictive Trends:** Linear regression model forecasts future sentiment patterns
- **Actionable Recommendations:** Data-driven insights for HR and management interventions

---

## **Key Technical Features**

✓ **Automated Sentiment Classification** - Processes unstructured text into structured sentiment labels  
✓ **Exploratory Data Analysis** - Comprehensive visualizations and statistical summaries  
✓ **Modular Design** - Separate scripts for each analysis component (scalable & maintainable)  
✓ **Clear Visualization** - Generates interpretable charts (`Figure_1.png`) for stakeholder reporting  
✓ **Trend Tracking** - Monthly aggregation and time-series analysis  
✓ **Predictive Modeling** - Linear regression for sentiment forecasting  
✓ **Risk Scoring** - Quantitative employee risk assessment and ranking  

---

## **Skills Demonstrated**

This project showcases:

- **Data Analysis:** Pandas data manipulation, exploratory data analysis (EDA), statistical analysis
- **Machine Learning:** Sentiment classification, linear regression modeling, risk prediction
- **Natural Language Processing:** Text processing and sentiment classification techniques
- **Data Visualization:** Creating clear, actionable charts for insights (Figure_1.png)
- **Python Programming:** Writing modular, well-organized code across multiple scripts
- **Problem-Solving:** Translating business needs (flight risk) into data science solutions
- **Time-Series Analysis:** Monthly sentiment tracking and trend forecasting
- **Communication:** Clear documentation and visualization of findings

---

## **Relevance to Student Support & Program Assessment**

**Application to Educational Programs:**

The methodologies used in this employee sentiment project are directly applicable to student support and program assessment:

- **Sentiment → Student Engagement:** Analyze student feedback to understand satisfaction and engagement
- **Flight Risk → Student Retention:** Identify students likely to drop out or leave programs early
- **Trend Analysis → Program Effectiveness:** Track program outcomes and effectiveness over time
- **Risk Ranking → Targeted Support:** Prioritize support resources for at-risk students
- **Predictive Modeling:** Forecast which students need additional support before issues escalate

This demonstrates understanding of how data-driven insights improve retention and outcomes in educational and career services settings.

---

## **Results**

The project successfully demonstrates:
- Classification of employee sentiment with accuracy and consistency
- Identification of key patterns in employee feedback
- Prediction of flight risk indicators using data-driven methodology
- Generation of actionable insights for HR and organizational decision-making
- Value of combining NLP with machine learning for business analytics

---

## **Author**

**Venkata Rajesh Kadamba**  
Data Analyst | Graduate Student (MS Computer and Information Science)  
Virginia Commonwealth University  

**Contact:** charanrajesh9963@gmail.com  
**LinkedIn:** linkedin.com/in/charan-rajesh594705285  
**GitHub:** github.com/charanrajesh1  
**Phone:** (804) 301-8578  

---

## **Future Enhancements**

Potential improvements to extend this project:

- **Advanced NLP:** Implement transformer models (BERT, GPT) for sophisticated sentiment analysis
- **Deep Learning:** Use neural networks for improved classification accuracy
- **Real-time Processing:** Build pipeline to process feedback continuously
- **Interactive Dashboard:** Create Tableau/Power BI dashboard for stakeholder access
- **Causal Analysis:** Identify root causes of negative sentiment
- **Outcome Correlation:** Link predictions to actual turnover data
- **Multi-language Support:** Extend to analyze feedback in multiple languages
- **Semantic Analysis:** Understand specific themes and topics in feedback beyond sentiment

---

## **Notes**

This project demonstrates the power of combining data science with organizational analytics. By quantifying employee sentiment and predicting flight risk, organizations can take proactive steps to improve retention and organizational health.

The same data-driven approach is highly applicable to educational programs, where tracking student sentiment and identifying at-risk students leads to improved retention and program outcomes.

---

## **License**

This project is open source and available for educational and professional use.
