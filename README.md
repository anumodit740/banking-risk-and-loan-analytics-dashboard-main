# Banking Risk & Loan Analytics Dashboard (Power BI)

## Project Overview

This project focuses on risk analytics in banking and financial services using Power BI. The goal is to analyze client profiles, loan exposure, deposits, fees, income segments, and risk indicators to help banks make better lending and portfolio decisions.

### Core Problem Statement

Develop a basic understanding of risk analytics in banking and financial services and understand how data can be used to minimize the risk of financial loss while lending to customers.

### Solution

The dashboard enables banks to make data-driven decisions by analyzing customer financial behavior, income bands, loan exposure, deposits, credit card balances, and risk-related indicators. It helps decision-makers identify customer segments, understand loan distribution, and assess repayment-related risk factors.

---

## Dashboard Key Features & Views

| Dashboard View        | Primary Focus                                                      | Key Metrics                                                                |
| :-------------------- | :----------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **Home / Summary**    | High-level performance snapshot and critical risk exposure metrics | Total Clients, Total Loan, Total Deposit, Total Fees                       |
| **Loan Analysis**     | Deep dive into lending activity and borrower risk profiles         | Bank Loan by Income Band, Business Lending, Credit Card Balance            |
| **Deposit Analysis**  | Insights into customer liquidity and funding sources               | Bank Deposits, Savings Account, Checking Account, Foreign Currency Account |
| **Summary Dashboard** | Executive-level summary of financial and customer performance      | Engagement Length, Processing Fees, Total Loan, Total Deposit              |

---

## Dashboard Visualizations

### 1. Home Dashboard

This page provides a high-level overview of total clients, key monetary figures, customer distribution, and navigation across the report.

<img width="1203" height="663" alt="Home" src="https://github.com/user-attachments/assets/a164f9a6-d193-456b-b65a-f084e01fea42" />

### 2. Loan Analysis Dashboard

This page focuses on loan distribution, risk segmentation by income band, lending activity, and customer borrowing behavior.

<img width="1176" height="654" alt="Loan Analysis" src="https://github.com/user-attachments/assets/83ded882-bf07-4d07-81cf-b9eba7374ae2" />

### 3. Deposit Analysis Dashboard

This page provides an overview of customer deposits and account balances across different account types.

<img width="1167" height="649" alt="Deposit Analysis" src="https://github.com/user-attachments/assets/60426b50-78e0-4d11-9962-a1ba2bf1b65e" />

### 4. Summary Dashboard

This page provides executive-level insights into client engagement, financial performance, and key banking metrics.

<img width="1659" height="913" alt="Summary" src="https://github.com/user-attachments/assets/b1dc7d57-3da1-497b-a0b9-559c8a302610" />

---

## Project Structure

```text
banking-risk-and-loan-analytics-dashboard-main
│
├── Analysis
│   └── BankEDA.py
│
├── Dashboard
│   └── Banking Dashboard.pbix
│
├── Datasets
│   └── Banking.csv
│
├── Documentation
│   ├── EDA_Findings.md
│   └── Business_Insights.md
│
└── README.md
```

---

## Technical Stack

* **Power BI Desktop** - Dashboard development and data visualization
* **DAX** - KPI and calculated measure creation
* **Python** - Exploratory data analysis
* **Pandas** - Data loading and analysis
* **NumPy** - Numerical operations
* **Matplotlib & Seaborn** - EDA visualizations

---

## Data Model

The project uses multiple banking-related tables such as:

* `Client-Banking`
* `Banking Relationship`
* `Gender`
* `Investment Advisor`
* `Period`

These tables help analyze customer demographics, financial relationships, loan behavior, deposits, and banking engagement.

---

## Data Preparation Highlights

* **Income Band Creation:** Customers were segmented into income groups such as Low, Mid, and High income bands.
* **Engagement Timeframe:** Customer engagement duration was calculated using the joining date.
* **Processing Fees:** Processing fee calculation was created using the fee structure field.
* **Risk Segmentation:** Customers were analyzed based on loan exposure, income level, deposits, and banking behavior.

---

## Exploratory Data Analysis (EDA)

EDA was performed using Python to understand customer banking behavior, financial patterns, risk indicators, and relationships between major banking variables.

### Key EDA Tasks

* Data loading and initial inspection
* Missing value analysis
* Descriptive statistics
* Income band segmentation
* Categorical variable analysis
* Numerical distribution analysis
* Correlation analysis
* Relationship analysis between deposits, loans, savings, income, and business lending

EDA Script: [`Analysis/BankEDA.py`](Analysis/BankEDA.py)

---

## Key Performance Indicators (KPIs)

| Metric              | Calculation / Definition                                                              |
| :------------------ | :------------------------------------------------------------------------------------ |
| **Total Loan**      | Sum of Bank Loan, Business Lending, and Credit Card Balance                           |
| **Total Deposit**   | Sum of Bank Deposits, Savings Account, Checking Account, and Foreign Currency Account |
| **Total Fees**      | Total amount charged through account setup and maintenance fees                       |
| **Engagement Days** | Duration of customer relationship with the bank                                       |
| **Income Band**     | Customer segmentation based on estimated income                                       |

---

## Business Insights

* Customers with higher deposits generally maintain higher savings balances.
* Income level strongly influences banking product usage and loan exposure.
* Business lending customers show different borrowing behavior compared to retail customers.
* Deposit and savings account balances show a strong positive relationship.
* Risk analysis becomes more effective when customer income, loan amount, deposits, and engagement duration are analyzed together.

---

## Project Outcomes

* Built an interactive Power BI dashboard for banking risk and loan analysis.
* Created KPIs for loans, deposits, fees, income bands, and customer engagement.
* Performed Python-based EDA to understand financial patterns and customer behavior.
* Designed multiple dashboard pages for loan analysis, deposit analysis, and executive summary.
* Converted raw banking data into actionable business insights for lending risk assessment.

---

## How to Use

1. Install **Power BI Desktop**.
2. Clone this repository to your local machine.
3. Open the `Banking Dashboard.pbix` file from the `Dashboard` folder.
4. Explore the report using slicers, filters, and dashboard pages.
5. Review the Python EDA script in `Analysis/BankEDA.py`.

---

## Created By

**Anumodit Shukla**

***
