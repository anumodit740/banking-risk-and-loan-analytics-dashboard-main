# 🏦 Banking Risk & Loan Analytics Dashboard
> **Power BI Data Analytics Project**
> *Developed by Anumodit Shukla*

---

## 📌 Project Overview

This project focuses on **risk analytics within the banking and financial services sector**. Utilizing Power BI, this interactive dashboard assists financial institutions in evaluating loan repayment probabilities, understanding funding stability, and minimizing credit risk exposure.

### 🎯 Core Problem Statement
To build a comprehensive risk assessment framework that evaluates applicant profiles against key risk indicators, minimizing capital loss while optimizing lending operations.

### 💡 The Solution
An end-to-end analytics dashboard that empowers credit managers and executives to make data-driven lending decisions. By instantly evaluating income bands, liability exposure, and liquidity profiles, the bank can proactively identify high-risk applicants and mitigate default rates.

---

## 🗺️ Dashboard Architecture & Views

The report is structured into four distinct analytical layers to provide a 360-degree view of the bank's financial ecosystem:

| View | 🎯 Primary Focus | 📊 Key Metrics Included |
| :--- | :--- | :--- |
| **Home / Summary** | High-level executive performance snapshot & critical risk exposure. | Total Clients, Total Loan, Total Deposit, Total Fees |
| **Loan Analysis** | Credit distribution & borrower risk segmentation. | Loan by Income Band, Business Lending, Credit Card Trends |
| **Deposit Analysis** | Client liquidity evaluation & internal funding sources. | Total Deposit, Savings Balances, Foreign Currency Exposure |
| **Summary Dashboard** | Historical performance trends & client relationship value. | Engagement Length, Processing Fees, Yield Ratios |

---

## 📊 Dashboard Interface & Visualizations

### 1️⃣ Home Dashboard
*The central hub of the application, featuring high-level KPIs, global client distribution, and seamless cross-page navigation.*

<img width="1203" height="663" alt="Home" src="https://github.com/user-attachments/assets/a164f9a6-d193-456b-b65a-f084e01fea42" />

---

### 2️⃣ Loan Analysis Dashboard
*Deep dive into credit risk. This view segments outstanding balances by borrower income categories to isolate potential credit bottlenecks.*

<img width="1176" height="654" alt="Loan Analysis" src="https://github.com/user-attachments/assets/83ded882-bf07-4d07-81cf-b9eba7374ae2" />

---

### 3️⃣ Deposit Analysis Dashboard
*Monitors the asset-liability balance by tracking stable funding sources across various client checking and savings vehicles.*

<img width="1167" height="649" alt="Deposit Analysis" src="https://github.com/user-attachments/assets/60426b50-78e0-4d11-9962-a1ba2bf1b65e" />

---

### 4️⃣ Summary Dashboard
*An executive-level look at operational efficiency, tracking customer lifecycle value and fee structures over time.*

<img width="1659" height="913" alt="Summary" src="https://github.com/user-attachments/assets/b1dc7d57-3da1-497b-a0b9-559c8a302610" />

---

## 🛠️ Technical Stack & Data Model

* **Core BI Engine:** Microsoft Power BI Desktop
* **Modeling & Analytics:** Data Analysis Expressions (DAX)
* **Data Schema:** Interlinked Star/Snowflake schema comprising tables: `Banking Relationship`, `Client-Banking`, `Gender`, `Investment Advisor`, and `Period`.

### ⚡ Data Preparation & Feature Engineering
* **Risk Categorization:** Engineered custom conditional logic to segment client profiles into targeted risk buckets: **Low Income Band** (`< 100,000`) and **Mid Income Band** (`< 300,000`).
* **Tenure Tracking:** Calculated explicit `Engagement Days` derived from the delta between client onboarding dates and the reporting period.
* **Revenue Parsing:** Extracted operational margins by calculating distinct `Processing Fees` tied directly to categorical `Fee Structures`.

### 📈 Core KPI Metrics

 ---

## 🚀 Future Roadmap

* **Investor Profiling:** Segment underwriting sources to evaluate loan concentration risks across distinct institutional investor brackets.
* **Competitive Market Strategy:** Benchmarking market-share capture across various banking models (e.g., Private vs. Public) to guide customer acquisition strategies.
* **Geographical Risk Modeling:** Mapping credit allocations against demographic and national origins to identify macroeconomic risk concentrations.

---
