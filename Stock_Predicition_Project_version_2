import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("apple.csv", skiprows=[1])
data = data.dropna()

X = data[["Open", "High", "Low", "Volume"]]
y = data["Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)

average_close = data["Close"].mean()
median_close = data["Close"].median()
highest_price = data["High"].max()
lowest_price = data["Low"].min()
average_volume = data["Volume"].mean()

data["Daily Return"] = data["Close"].pct_change()
data = data.dropna()
expected_value = data["Daily Return"].mean()

if expected_value > 0:
    ev_result = "Positive"

elif expected_value < 0:
    ev_result = "Negative"

else:
    ev_result = "Neutral"

volatility = data["Daily Return"].std()

if volatility < 0.01:
    volatility_level = "Low"

elif volatility < 0.02:
    volatility_level = "Medium"

else:
    volatility_level = "High"


risk_level = volatility_level

positive_days = (data["Daily Return"] > 0).sum()
negative_days = (data["Daily Return"] < 0).sum()
total_days = positive_days + negative_days
positive_probability = (positive_days / total_days) * 100
negative_probability = (negative_days / total_days) * 100

skewness = data["Daily Return"].skew()

if -0.5 <= skewness <= 0.5:
    distribution = "Approximately Normal"

elif skewness > 0.5:
    distribution = "Positively Skewed"

else:
    distribution = "Negatively Skewed"

correlation = data["Close"].corr(data["Volume"])

if correlation > 0.5:
    correlation_result = "Strong Positive"

elif correlation < -0.5:
    correlation_result = "Strong Negative"

else:
    correlation_result = "Weak"


if expected_value > 0 and volatility_level == "Low":
    outlook = "Historically Stable"

elif expected_value > 0:
    outlook = "Moderate Growth Potential"

else:
    outlook = "Uncertain"


print("=" * 55)
print("      MACHINE LEARNING MARKET EXPECTATION REPORT")
print("=" * 55)

print("\nMachine Learning")
print("-" * 30)
print("R2 Score :", round(r2,4))
print("Model Confidence :", "High" if r2 > 0.90 else "Medium")

print("\nStatistics")
print("-" * 30)
print("Average Closing Price :", round(average_close,2))
print("Median Closing Price :", round(median_close,2))
print("Highest Price :", round(highest_price,2))
print("Lowest Price :", round(lowest_price,2))
print("Average Volume :", round(average_volume))

print("\nMarket Analysis")
print("-" * 30)
print("Distribution :", distribution)
print("Expected Value :", ev_result)
daily_return = round(expected_value * 100, 2)

if daily_return > 0:
    print(f"Average Daily Return : +{daily_return}%")

elif daily_return < 0:
    print(f"Average Daily Return : {daily_return}%")

else:
    print("Average Daily Return : 0.00%")
print("Volatility :", volatility_level)
print("Risk Level :", risk_level)

print("\nProbability")
print("-" * 30)
print("Positive Days :", round(positive_probability,2), "%")
print("Negative Days :", round(negative_probability,2), "%")

print("\nCorrelation")
print("-" * 30)
print("Close vs Volume :", correlation_result)

print("\nMarket Outlook")
print("-" * 30)
print(outlook)

print("\nDisclaimer")
print("-" * 30)
print("This report is generated from historical data.")
print("It is for educational purposes only.")
print("It does not predict future prices or provide investment advice.")
print("check company's future projects to get more confident")
