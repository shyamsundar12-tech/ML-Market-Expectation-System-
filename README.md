
# 📈 ML Market Expectation System

A machine learning and statistical market analysis project developed during my **ReTech internship**, progressing through three versions from a basic Linear Regression model to an interactive **Streamlit dashboard**.

The project analyzes historical market data using **Machine Learning, statistical analysis, probability, volatility, and data visualization** to generate a Market Expectation Report.

> ⚠️ **Educational Project:** This system is designed for learning and analytical purposes. It does not guarantee future market prices and should not be considered financial or investment advice.

---

## 🚀 Project Evolution

### Version 1 — Basic Machine Learning Model

The first version establishes the core Machine Learning workflow using **Linear Regression**.

The model uses:

* Open
* High
* Low
* Volume

as input features and **Close** as the target variable.

The dataset is split into **80% training and 20% testing data**, after which the Linear Regression model is trained and evaluated using the **R² score**.

The program also calculates basic market statistics:

* Average Closing Price
* Highest Price
* Lowest Price
* Average Volume

---

### Version 2 — Market Expectation Analysis

Version 2 expands the project from a basic ML model into a broader **Market Expectation System**.

In addition to Linear Regression, it introduces statistical market analysis using historical daily returns.

#### 📊 Statistical Analysis

The system calculates:

* Average Closing Price
* Median Closing Price
* Highest Price
* Lowest Price
* Average Volume
* Expected Daily Return
* Volatility
* Risk Level
* Distribution / Skewness
* Positive Return Probability
* Negative Return Probability
* Close vs Volume Correlation
* Market Outlook

## The system also classifies historical market behavior into categories such as **Low, Medium, and High volatility**, and generates a historical market outlook based on expected return and volatility.

### Version 3 — Interactive Streamlit Dashboard

Version 3 introduces an interactive **Streamlit web dashboard**.

The dashboard provides a graphical interface for exploring the market analysis system instead of relying only on terminal output.

Users can select:

* Apple dataset
* Gold dataset
* Their own CSV dataset

The dashboard combines the Machine Learning and statistical components developed in the previous versions.

#### 🤖 Machine Learning Dashboard

The dashboard displays:

* Linear Regression model
* R² Score
* Train/Test performance
* Model information
* Dataset summary

#### 📊 Market Expectation Dashboard

It displays:

* Return distribution
* Expected value
* Volatility
* Risk
* Positive-day probability
* Negative-day probability
* Close/Volume correlation
* Historical market outlook

#### 📈 Interactive Visualizations

Version 3 includes:

* Closing Price Trend
* Trading Volume
* Daily Return
* Closing Price Summary
* Volume Summary
* Dataset Information
* Machine Learning Model Information

---

## 🧠 Machine Learning Workflow

```text
Historical Market Data
        ↓
Data Loading
        ↓
Data Cleaning
        ↓
Feature Selection
        ↓
Open ─┐
High ─┤
Low ──┤──→ Linear Regression ──→ Predicted Close
Volume┘
        ↓
      R² Score
        ↓
Model Evaluation
```

The project uses **Linear Regression** from Scikit-learn. The selected features are Open, High, Low, and Volume, while Close is used as the target variable.

---

## 📐 Statistical Analysis Workflow

```text
Closing Price
      ↓
Daily Returns
      ↓
 ┌────┼───────────────┐
 ↓    ↓       ↓       ↓
Mean  Vol.  Skewness Probability
 ↓     ↓       ↓        ↓
Expected  Risk   Distribution  Positive/Negative
Return
      ↓
Correlation Analysis
      ↓
Historical Market Outlook
```

Daily returns are calculated from consecutive closing prices and are used for expected-value, volatility, probability, and distribution analysis.

---

## 🛠️ Technologies Used

| Technology            | Purpose                       |
| --------------------- | ----------------------------- |
| **Python**            | Core programming language     |
| **Pandas**            | Data loading and manipulation |
| **NumPy**             | Numerical computation         |
| **Scikit-learn**      | Machine Learning              |
| **Linear Regression** | Market prediction model       |
| **Streamlit**         | Interactive dashboard         |
| **CSV**               | Historical market datasets    |

---

## 📂 Project Versions

```text
ML-Market-Expectation-System/
│
├── stock_project_v1.py
├── stock_project_v2.py
├── stock_V3.py
│
├── apple.csv
├── Gold_DS.csv
│
└── README.md
```

### Version Summary

| Version | Main Development                            |
| ------- | ------------------------------------------- |
| **V1**  | Basic Linear Regression + Market Statistics |
| **V2**  | Market Expectation + Statistical Analysis   |
| **V3**  | Interactive Streamlit Dashboard             |

---

## ▶️ How to Run Version 1 & Version 2

Install the required libraries:

```bash
pip install pandas numpy scikit-learn
```

Run Version 1:

```bash
python stock_project_v1.py
```

Run Version 2:

```bash
python stock_project_v2.py
```

---

## 🌐 How to Run Version 3

Install Streamlit and the required libraries:

```bash
pip install streamlit pandas numpy scikit-learn
```

Run the dashboard:

```bash
python -m streamlit run stock_V3.py
```

The Streamlit application will open in your browser.

---

## 📊 Dataset Requirements

The project works with historical market data containing columns such as:

```text
Date
Open
High
Low
Close
Volume
```

Version 3 also provides an option to upload a custom CSV dataset through the dashboard.

---

## 📌 Key Learning Outcomes

Through the progression of the three versions, this project demonstrates practical experience with:

* Python programming
* Data preprocessing
* Pandas DataFrames
* Feature and target selection
* Train/Test splitting
* Linear Regression
* Model evaluation using R²
* Statistical analysis
* Daily return calculation
* Volatility analysis
* Probability analysis
* Correlation analysis
* Data visualization
* Streamlit dashboard development
* Building an ML project incrementally

---

## ⚠️ Limitations

This project is based on **historical market data**.

Financial markets are affected by many factors that are not included in this model, including news, macroeconomic conditions, market sentiment, company fundamentals, geopolitical events, and unexpected market movements.

Therefore, the results should be interpreted as **historical data analysis and educational experimentation**, not as guaranteed future predictions.

The Version 2 implementation itself explicitly states that the report is based on historical data and does not provide future-price prediction or investment advice.

---

## 🔮 Future Improvements

Potential future improvements include:

* Time-series forecasting models
* Random Forest and Gradient Boosting models
* LSTM/GRU neural networks
* Improved time-series train/test methodology
* Additional technical indicators
* Real-time market data integration
* Model comparison
* Interactive prediction inputs
* Advanced visualization
* Model persistence and deployment
* Improved dashboard design

---

## 👨‍💻 Project Background

This project was developed as part of my **ReTech internship**, where I progressively developed the system from a basic Machine Learning implementation into a statistical market analysis application and finally an interactive Streamlit dashboard.

The three versions demonstrate the evolution of the project from **core ML implementation → statistical market analysis → interactive application development**.

---

## ⚖️ Disclaimer

This project is created for **educational and learning purposes only**.

It should not be considered financial advice, investment advice, or a guaranteed stock/market prediction system.

**Always perform independent research before making any financial decision.**
