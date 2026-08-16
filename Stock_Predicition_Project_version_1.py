import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("Gold_DS.csv")
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

print("Model Performance")
print("------------------------")
print("R2 Score :", round(r2,4))

print("\nMarket Statistics")
print("------------------------")

print("Average Closing Price :", round(data["Close"].mean(),2))
print("Highest Price :", data["High"].max())
print("Lowest Price :", data["Low"].min())
print("Average Volume :", round(data["Volume"].mean()))

print("\nProject Completed Successfully!")
