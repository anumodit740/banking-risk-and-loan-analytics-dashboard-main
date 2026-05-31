import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# =========================
# 1. Load Dataset
# =========================

df = pd.read_csv("Datasets/Banking.csv")

print("First 5 rows:")
print(df.head())

print("\nShape of the DataFrame:")
print(df.shape)

print("\nDataFrame Info:")
print(df.info())


# =========================
# 2. Feature Engineering
# =========================

bins = [0, 100000, 300000, float("inf")]
labels = ["Low", "Mid", "High"]

df["Income Band"] = pd.cut(
    df["Estimated Income"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

df["Joined Bank"] = pd.to_datetime(df["Joined Bank"], format="%d-%m-%Y")

print("\nJoined Bank dtype:")
print(df["Joined Bank"].dtype)


# =========================
# 3. Categorical Analysis
# =========================

categorical_cols = [
    "Risk Weighting",
    "Nationality",
    "Occupation",
    "Fee Structure",
    "Loyalty Classification",
    "Properties Owned",
    "Income Band"
]

for col in categorical_cols:
    print(f"\nValue Counts for '{col}':")
    print(df[col].value_counts())


# =========================
# 4. Numerical Summary
# =========================

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# =========================
# 5. Univariate Analysis
# =========================

numerical_cols = [
    "Fee Structure",
    "Age",
    "Estimated Income",
    "Superannuation Savings",
    "Credit Card Balance",
    "Bank Loans",
    "Bank Deposits",
    "Checking Accounts",
    "Saving Accounts",
    "Foreign Currency Account",
    "Business Lending"
]

plt.figure(figsize=(15, 10))

for i, col in enumerate(numerical_cols):
    plt.subplot(4, 3, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(col)

plt.tight_layout()
plt.show()


# =========================
# 6. Correlation Analysis
# =========================

correlation_cols = [
    "Age",
    "Estimated Income",
    "Superannuation Savings",
    "Credit Card Balance",
    "Bank Loans",
    "Bank Deposits",
    "Checking Accounts",
    "Saving Accounts",
    "Foreign Currency Account",
    "Business Lending",
    "Properties Owned"
]

correlation_matrix = df[correlation_cols].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of Numerical Features")
plt.tight_layout()
plt.show()


# =========================
# 7. Relationship Analysis
# =========================

pairs_to_plot = [
    ("Bank Deposits", "Saving Accounts"),
    ("Checking Accounts", "Saving Accounts"),
    ("Checking Accounts", "Foreign Currency Account"),
    ("Age", "Superannuation Savings"),
    ("Estimated Income", "Checking Accounts"),
    ("Bank Loans", "Credit Card Balance"),
    ("Business Lending", "Bank Loans"),
]

for x_col, y_col in pairs_to_plot:
    plt.figure(figsize=(8, 6))
    sns.regplot(
        data=df,
        x=x_col,
        y=y_col,
        scatter_kws={"alpha": 0.4},
        line_kws={"color": "red"}
    )
    plt.title(f"Relationship between {x_col} and {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()
    plt.show()


# =========================
# 8. Key Insights
# =========================

print("""
KEY INSIGHTS

1. Deposits and Savings Behavior
Bank Deposits and Saving Accounts appear strongly related. This suggests that customers who maintain higher deposits also tend to maintain stronger savings balances.

2. Income, Age, and Accumulation
Age and Estimated Income show moderate relationships with savings, checking balances, and superannuation savings. This reflects the financial lifecycle pattern where older or higher-income customers accumulate more financial assets.

3. Low Correlation with Properties Owned
Property ownership has weaker relationships with banking variables, suggesting it may depend on external factors such as location, inheritance, or real estate conditions.

4. Business vs Personal Banking
Business Lending has some relationship with Bank Loans, suggesting some customers may use both personal and business credit products.
""")