# 🚀 Customer Orders ETL Pipeline  
### Python • Pandas • Data Engineering Fundamentals

<p align="center">
  <img src="assets/etl_pipeline.gif" width="700"/>
</p>

---

## 🧠 Project Overview

This project demonstrates a **production-style ETL pipeline** built using **Python and Pandas**.  
It transforms raw customer and order data into an **analytics-ready dataset**, following best practices used in real-world data engineering pipelines.

The logic and structure closely resemble workflows orchestrated using **Airflow**, processed using **Dataproc**, and consumed in **BigQuery**.

---

## 🎯 Business Problem

Given raw datasets:
- 👤 Customers
- 🧾 Orders  

The objective is to:
- Clean and standardize raw data
- Handle missing values safely
- Filter valid transactions
- Aggregate key business metrics
- Enrich data using customer master information
- Generate a final dataset ready for analytics and reporting

---

## 🛠️ ETL Pipeline Flow (Logical Steps)

# 🚀 Customer Orders ETL Pipeline  
### Python • Pandas • Data Engineering Fundamentals

<p align="center">
  <img src="assets/etl_pipeline.gif" width="700"/>
</p>

---

## 🧠 Project Overview

This project demonstrates a **production-style ETL pipeline** built using **Python and Pandas**.  
It transforms raw customer and order data into an **analytics-ready dataset**, following best practices used in real-world data engineering pipelines.

The logic and structure closely resemble workflows orchestrated using **Airflow**, processed using **Dataproc**, and consumed in **BigQuery**.

---

## 🎯 Business Problem

Given raw datasets:
- 👤 Customers
- 🧾 Orders  

The objective is to:
- Clean and standardize raw data
- Handle missing values safely
- Filter valid transactions
- Aggregate key business metrics
- Enrich data using customer master information
- Generate a final dataset ready for analytics and reporting

---

## 🛠️ ETL Pipeline Flow (Logical Steps)

📂 Raw CSV Files
│
▼
📥 Read Data (Pandas)
│
▼
🧹 Clean Column Names
│
▼
🚨 Handle Missing Values
│
▼
✅ Filter Completed Orders
│
▼
📊 Aggregate Order Amounts
│
▼
🔗 Join Customer Master Data
│
▼
📤 Final Analytics Output (CSV)


---

## 🖼️ Visual Pipeline Diagram

<p align="center">
  <img src="assets/etl_pipeline.png" width="700"/>
</p>

> 💡 This pipeline follows the same logical structure used in Airflow-orchestrated GCP data pipelines.

---

## 📁 Project Structure

python_pandas_etl/
│
├── assets/
│ ├── etl_pipeline.png
│ └── etl_pipeline.gif
│
├── data/
│ ├── customers.csv
│ └── orders.csv
│
├── output/
│ └── customer_order_summary.csv
│
├── etl.py # Step-by-step learning version
├── final_etl.py # Production-style modular ETL
└── README.md


---

## 📊 Final Output Schema

| Column | Description |
|------|------------|
| customer_id | Unique customer identifier |
| customer_name | Customer name |
| city | Customer city |
| total_order_amount | Total completed order value |

📄 Output file:
output/customer_order_summary.csv


---

## 🧩 Key Transformations

### 🧹 Data Cleaning
- Standardized column names (lowercase, underscores)
- Ensured SQL / BigQuery compatibility

### 🚨 Data Quality Handling
- Identified missing values in order data
- Applied business rules (`order_amount = 0`)

### 📊 Aggregation
- Grouped orders by customer
- Calculated total completed order value

### 🔗 Data Enrichment
- Joined aggregated order data with customer master data

---

## 🧠 Engineering Design Principles

- Modular Python functions for each ETL stage
- Clear pipeline orchestration via `main()`
- Production-style design aligned with Airflow task patterns

---



## 🌱 Future Enhancements

- 🔄 Convert pipeline to **PySpark** for Dataproc
- ☁️ Load output directly into **BigQuery**
- 🕒 Orchestrate pipeline using **Apache Airflow**

---

⭐ If you find this project useful, feel free to star the repository!
